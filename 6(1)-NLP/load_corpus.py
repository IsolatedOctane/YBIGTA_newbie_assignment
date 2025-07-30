from datasets import load_dataset
from transformers import AutoTokenizer
from typing import List

def load_corpus() -> List[str]:
    # 데이터셋 불러오기
    dataset = load_dataset("google-research-datasets/poem_sentiment", split="train")

    # 토크나이저 불러오기
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    max_token_len = 512

    # verse_text만 추출하며, 512 토큰 이하만 필터링
    corpus = [
        sample["verse_text"]
        for sample in dataset
        if len(tokenizer(sample["verse_text"], truncation=True, max_length=max_token_len)["input_ids"]) <= max_token_len
    ]

    return corpus
