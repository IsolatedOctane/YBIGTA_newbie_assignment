from lib import Trie
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
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        # 구현하세요!
        for i in trie[pointer].children:
            if element==trie[i].body:
                pointer=i
                break

    return cnt + int(len(trie[0].children) == 1)


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