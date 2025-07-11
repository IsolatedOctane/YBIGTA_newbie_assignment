from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    """
    update를 bottom-up 방식으로 구현함

    """
    def __init__(self, n):
        """
        n개의 element의 segment tree를 할당
        """
        self.size: int = 1
        while self.size<n:
            self.size*=2
        self.tree: list[int] = [0] * (2* self.size)
        self.size-=1 #1-indexed



    def update(self, index: int, diff: int):
        """
        배열의 index번째 element의 값이 diff만큼 변했을때,
        segment tree 내부의 값을 조정한다.
        """
        tree_index: int = index +  self.size 
        while tree_index>0:
            self.tree[tree_index]+=diff
            tree_index//=2
