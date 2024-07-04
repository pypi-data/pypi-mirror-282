import torch
import torch.nn.functional as F
from enum import Enum
from typing import Tuple, Optional


class LFQ_MODE(Enum):
    VANILLA = 1
    X_BATCH = 2
    XY_APPROX = 3


def generate_sub_book(d: int, start: int, end: int) -> torch.Tensor:
    sub_indices = torch.arange(start, end).cuda()
    sub_book = (
        sub_indices.unsqueeze(-1)
        .bitwise_right_shift(torch.arange(d - 1, -1, -1).cuda())
        .remainder(2)
    )
    sub_book[sub_book == 0] = -1
    return sub_book.float()


class LFQ:
    def __init__(self, d: int = 26, x_split: int = 16, temperature: float = 1.0, eps: float = 1e-10, is_training: bool = False, debug: bool = False):
        self.d = d
        self.k = 2 ** d
        if self.d < 19:
            self.mode = LFQ_MODE.VANILLA
            indices = torch.arange(self.k).cuda()
            book = (
                indices.unsqueeze(-1)
                .bitwise_right_shift(torch.arange(d - 1, -1, -1).cuda())
                .remainder(2)
            )
            book[book == 0] = -1
            self.book_t = book.float().t()
        elif self.d < 26:
            self.mode = LFQ_MODE.X_BATCH
            # Initialize half book matrix
            indices = torch.arange(self.k // 2).cuda()
            self.half_book = (
                indices.unsqueeze(-1)
                .bitwise_right_shift(torch.arange(d - 1, -1, -1).cuda())
                .remainder(2)
            )
            self.half_book[self.half_book == 0] = -1
            self.half_book = self.half_book.float()
            self.x_split = x_split
            self.mean_probs = torch.zeros(self.k).cuda()
        else:
            self.mode = LFQ_MODE.XY_APPROX
            self.subbook_size = 2 ** 20
            self.num_subbooks = self.k // self.subbook_size
            self.x_split = x_split
            self.subbook_ranges = [(i * self.subbook_size, (i + 1) * self.subbook_size) for i in range(self.num_subbooks)]

        self.temperature = temperature
        self.eps = eps
        self.indices: Optional[torch.Tensor] = None
        self.is_training = is_training
        self.debug = debug
        self.commit_loss = None

    def entropy_from_half_logits(self, logits_half: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        a = F.softmax(logits_half, dim=-1)
        k_ = torch.sum(torch.exp(logits_half), dim=-1, keepdim=True)
        h_ = torch.sum(torch.exp(-logits_half), dim=-1, keepdim=True)
        c_ = k_ + h_
        m = a * k_ / c_
        n = a * h_ / c_
        log_m = torch.log(m)
        log_n = torch.log(n)
        e_m = -torch.sum(m * log_m, dim=-1)
        e_n = -torch.sum(n * log_n, dim=-1)
        e = e_m + e_n
        q = torch.cat([torch.mean(m, dim=0), torch.mean(n, dim=0)], dim=-1)
        return e, q

    def calc_entro_by_batch(self, x: torch.Tensor) -> Tuple[float, float, float]:
        assert (x.size(0) % self.x_split) == 0
        self.mean_probs.zero_()
        entro_mean = 0

        num_splits = x.size(0) // self.x_split
        for i in range(num_splits):
            x_chunk = x[i * self.x_split: (i + 1) * self.x_split]
            logits_half = x_chunk.float() @ self.half_book.t() / self.temperature
            entropy, mp = self.entropy_from_half_logits(logits_half)
            entro_mean += torch.sum(entropy).item() / x.size(0)
            self.mean_probs += mp
        self.mean_probs = self.mean_probs / num_splits
        mean_entro = -torch.sum(self.mean_probs * torch.log(self.mean_probs + self.eps))
        entro_loss = entro_mean - mean_entro
        return entro_mean, mean_entro, entro_loss

    def calc_entro_vanilla(self, x: torch.Tensor) -> Tuple[float, float, float]:
        logits = x.float() @ self.book_t
        l = logits / self.temperature
        probs = F.softmax(l, -1)
        log_probs = F.log_softmax(l + self.eps, -1)
        entropy = -torch.sum(probs * log_probs, -1)
        entro_mean = torch.mean(entropy)
        mean_probs = torch.mean(probs, 0)
        mean_entro = -torch.sum(mean_probs * torch.log(mean_probs + self.eps))
        entro_loss = entro_mean - mean_entro
        return entro_mean, mean_entro, entro_loss

    def calc_entro_xy_approx(self, x: torch.Tensor) -> Tuple[float, float, float]:
        entro_mean = 0
        mean_probs = torch.zeros(self.subbook_size).cuda()

        for start, end in self.subbook_ranges:
            sub_book = generate_sub_book(self.d, start, end)

            num_splits = x.size(0) // self.x_split
            for i in range(num_splits):
                x_chunk = x[i * self.x_split: (i + 1) * self.x_split]
                logits = x_chunk.float() @ sub_book.t()
                probs = F.softmax(logits / self.temperature, -1)
                log_probs = F.log_softmax(logits / self.temperature + self.eps, -1)
                entropy = -torch.sum(probs * log_probs, dim=1)
                entro_mean += torch.sum(entropy).item() / (
                        x.size(0) * len(self.subbook_ranges)
                )  # Adjust for subbooks
                mean_probs += torch.sum(probs, dim=0) / (
                        x.size(0) * len(self.subbook_ranges)
                )  # Adjust for subbooks

            if x.size(0) % self.x_split != 0:
                x_chunk = x[num_splits * self.x_split:]
                logits = x_chunk.float() @ sub_book.t()
                probs = F.softmax(logits / self.temperature, -1)
                log_probs = F.log_softmax(logits / self.temperature + self.eps, -1)
                entropy = -torch.sum(probs * log_probs, dim=1)
                entro_mean += torch.sum(entropy).item() / (
                        x.size(0) * len(self.subbook_ranges)
                )  # Adjust for subbooks
                mean_probs += torch.sum(probs, dim=0) / (
                        x.size(0) * len(self.subbook_ranges)
                )  # Adjust for subbooks

            # Delete tensors and empty cache to manage memory
            del sub_book, logits, probs, log_probs, entropy, x_chunk
            torch.cuda.empty_cache()

        mean_entro = -torch.sum(mean_probs * torch.log(mean_probs + self.eps))
        entro_loss = entro_mean - mean_entro
        return entro_mean, mean_entro, entro_loss

    def lfq_calc(self, x: torch.Tensor, return_indices: bool = False) -> Tuple[torch.Tensor, float, float, float, Optional[torch.Tensor]]:
        if self.mode == LFQ_MODE.VANILLA:
            entro_mean, mean_entro, entro_loss = self.calc_entro_vanilla(x)
        elif self.mode == LFQ_MODE.X_BATCH:
            entro_mean, mean_entro, entro_loss = self.calc_entro_by_batch(x)
        elif self.mode == LFQ_MODE.XY_APPROX:
            entro_mean, mean_entro, entro_loss = self.calc_entro_xy_approx(x)

        q = torch.where(x > 0, 1, -1).cuda()
        if self.is_training:
            q = x + (q - x).detach()
            self.commit_loss = F.mse_loss(x, q.detach(), reduction="none")

        if return_indices:
            binary_result = (q + 1) // 2
            powers_of_2 = 2 ** torch.arange(binary_result.size(-1) - 1, -1, -1).float().cuda()
            self.indices = (binary_result.float() @ powers_of_2).long()
        if self.debug:
            print(
                f"D: {self.d} EntroMean: {entro_mean:.2f}, MeanEntro: {mean_entro:.2f}, EntroLoss: {entro_loss:.2f}"
            )
        return q, entro_mean, mean_entro, entro_loss, self.indices, self.commit_loss

