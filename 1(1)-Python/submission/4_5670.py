from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        curr_index : int = 0
        found: bool = False
        for i in seq:
            found= False
            for child in self[curr_index].children:
                if self[child].body==i:
                    found=True
                    curr_index=child
                    break
            if not found:
                self.append(TrieNode(body=i))
                self[curr_index].children.append(len(self)-1)
                curr_index=len(self)-1
        self[curr_index].is_end=True





        pass

    # 구현하세요!


import sys

"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end or pointer==0:
            cnt += 1

        # 구현하세요!
        for i in trie[pointer].children:
            if element==trie[i].body:
                pointer=i
                break

    return cnt


def main() -> None:
    # 구현하세요!
    solution: int = 0


    

    while True:
        t : Trie[str] = Trie()
        solution=0
        try:
            n=int(sys.stdin.readline().strip())
        except:
            break
        user_input: list[str] = []
        for i in range(n):
            tmp=sys.stdin.readline().strip()
            t.push(tmp)
            user_input.append(tmp)
        
        for j in user_input:
            solution+=count(t,j)
        

        print(format(solution/n,".2f"))







if __name__ == "__main__":
    main()