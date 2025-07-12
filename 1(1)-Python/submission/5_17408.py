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
    def __init__(self, n) ->None:
        """
        n개의 element의 segment tree를 할당
        tree.size+1 부터 leaf node가 저장됨.
        """
        self.size: int = 1
        while self.size<n:
            self.size*=2
        self.tree: list[int] = [0] * (2* self.size)
        self.size-=1 #1-indexed



    def update(self, index: int, diff: int) -> None:
        """
        배열의 index번째 element의 값이 diff만큼 변했을때,
        segment tree 내부의 값을 조정한다.
        참고: index: 1-indexed
        """
        tree_index: int = index +  self.size 
        while tree_index>0:
            self.tree[tree_index]+=diff
            tree_index//=2



import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    pass


if __name__ == "__main__":
    main()