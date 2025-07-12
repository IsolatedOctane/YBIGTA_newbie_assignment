from lib import SegmentTree
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