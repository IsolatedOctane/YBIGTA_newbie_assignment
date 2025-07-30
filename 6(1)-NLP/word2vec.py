import torch
from torch import nn, Tensor
from torch.optim import Adam
from transformers import PreTrainedTokenizer
from typing import Literal


class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method

    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)

        # 토큰 인덱스 변환 (문장 단위 -> 토큰 리스트)
        token_ids = []
        for text in corpus:
            encoded = tokenizer(text, truncation=True, max_length=512)
            token_ids.extend(encoded["input_ids"])

        self.tokens = torch.tensor(token_ids, dtype=torch.long)

        # 특수 토큰 제거
        if tokenizer.cls_token_id is not None:
            self.tokens = self.tokens[self.tokens != tokenizer.cls_token_id]
        if tokenizer.sep_token_id is not None:
            self.tokens = self.tokens[self.tokens != tokenizer.sep_token_id]

        # 학습 함수 호출
        if self.method == "cbow":
            self._train_cbow(optimizer, criterion, num_epochs)
        elif self.method=="skipgram":
            self._train_skipgram(optimizer, criterion, num_epochs)

    def _train_cbow(
        self,
        optimizer: Adam,
        criterion: nn.Module,
        num_epochs: int
    ) -> None:
        data = []
        for i in range(self.window_size, len(self.tokens) - self.window_size):
            context = torch.cat([
                self.tokens[i - self.window_size:i],
                self.tokens[i + 1:i + 1 + self.window_size]
            ]).unsqueeze(0)  # (1, 2*window)
            target = self.tokens[i]
            data.append((context, target))

        for epoch in range(num_epochs):
            total_loss = 0.0
            for context, target in data:
                target = torch.tensor([target])  # (1,)

                optimizer.zero_grad()
                context_vectors = self.embeddings(context)
                context_mean = context_vectors.mean(dim=1)  # (1, d_model)
                logits = self.weight(context_mean)  # (1, vocab_size)

                loss = criterion(logits, target)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()

            print(f"[Epoch {epoch+1}] CBOW Loss: {total_loss:.4f}")

    def _train_skipgram(
        self,
        optimizer: Adam,
        criterion: nn.Module,
        num_epochs: int
    ) -> None:
        data = []
        for i in range(self.window_size, len(self.tokens) - self.window_size):
            targets = torch.cat([
                self.tokens[i - self.window_size:i],
                self.tokens[i + 1:i + 1 + self.window_size]
            ])
            context = self.tokens[i]
            for target in targets:
                data.append((context, target))

        for epoch in range(num_epochs):
            counts=0
            total_loss = 0.0
            for context, target in data:
                context = torch.tensor([context], device=self.embeddings.weight.device)
                target = torch.tensor([target], device=self.embeddings.weight.device)

                optimizer.zero_grad()
                context_vector = self.embeddings(context)  # (1, d_model)
                logits = self.weight(context_vector)       # (1, vocab_size)
                loss = criterion(logits, target)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            print(f"[Epoch {epoch+1}] Skip-gram Loss: {total_loss:.4f}")
