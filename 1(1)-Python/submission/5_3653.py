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
    def query(tree:SegmentTree,left:int, right:int) -> int:
        left+=tree.size
        right+=tree.size
        ans: int = 0
        while left<=right:
            if left%2==1:
                ans+=tree.tree[left]
                left+=1
            if right%2==0:
                ans+=tree.tree[right]
                right-=1
            left//=2
            right//=2
        return ans
    t: int = int(sys.stdin.readline())
    for i in range(t):
        nm : list[int] = list(map(int,sys.stdin.readline().split()))
        n : int = nm[0]
        m : int = nm[1]
        userinput : list[int] = list(map(int,sys.stdin.readline().split()))
        tree: SegmentTree[int,int] = SegmentTree(n+m)
        position: list[int]=[0]+[i+m for i in range(1,n+1)]
        top: int = m-1
        for j in range(1,n+1):
            tree.update(j+m,1)
        for k in userinput:
            print(query(tree, 1, position[k-1]),end=' ')
            tree.update(position[k],-1)
            position[k]=top
            top-=1
            tree.update(position[k],1)



        
        print()



    
    




if __name__ == "__main__":
    main()
