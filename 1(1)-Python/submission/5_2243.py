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


def main() -> None:
    # 구현하세요!
    def query(tree: SegmentTree, index: int, target: int ) -> int:
        """
        binary search
        index: 현재 탐색 중인 segtree의 index
        target: 찾고싶은 맛 순위
        """
        if index> tree.size:
            return index-tree.size
        else:
            left: int = tree.tree[2*index] #left child 순위
            if target>left: #오른쪽 자식에 찾고싶은 맛 존재 
                return query(tree, 2*index+1, target-left)
            else: #왼쪽 자식에 찾고싶은 맛 존재 
                return query(tree, 2*index, target)

    N: int = 1000000 #맛 최대값
    n: int = int(sys.stdin.readline())
    Mytree:SegmentTree[int,int] = SegmentTree(N) #세그먼트 트리
    for i in range(n):
        userinput : list[int] = list(map(int,sys.stdin.readline().split()))
        if userinput[0] == 1:
            tmp: int = query(Mytree,1,userinput[1])
            print(tmp)
            Mytree.update(tmp, -1)
        else:
            Mytree.update(userinput[1],userinput[2])



    


if __name__ == "__main__":
    main()