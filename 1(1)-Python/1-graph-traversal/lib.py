from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        """
        self.n = n
        # 구현하세요!
        self.graph: DefaultDict[int,List[int]] = defaultdict(list)
        self.visited_dfs: List[bool] =[False for i in range(n+1)]
        self.visited_bfs: List[bool] =[False for i in range(n+1)]
        self.dfs_solution : List[int] = []
        self.bfs_solution : List[int] = []


    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        """
        # 구현하세요!
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현
        """
        # 구현하세요!
        self.dfs_solution = []
        self.visited_dfs = [False] * (self.n + 1)
        def _dfs(cur:int):
            self.visited_dfs[cur]=True
            self.dfs_solution.append(cur)
            for i in sorted(self.graph[cur]):
                if not self.visited_dfs[i]:
                    _dfs(i)
        _dfs(start)
        return self.dfs_solution


    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현
        """
        # 구현하세요!
        self.bfs_solution=[]
        q=deque([start])
        self.visited_bfs = [False] * (self.n + 1)
        self.visited_bfs[start]=True
        while q:
            curr=q.popleft()
            self.bfs_solution.append(curr)
            for i in sorted(self.graph[curr]):
                if not self.visited_bfs[i]:
                    self.visited_bfs[i]=True
                    q.append(i)

        return self.bfs_solution
    
    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
