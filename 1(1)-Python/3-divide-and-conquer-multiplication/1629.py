# lib.py의 Matrix 클래스를 참조하지 않음
import sys

"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용, 시간복잡도 고민!

    재귀함수로 푼다.
    홀수면 base^(exp/2) * base^(exp/2) * 

    또한... mod의 성질을 잘 이용해보자.

    base case: exp=0: 1

    """
    # 구현하세요!
    if exp==0:
        return 1
    else:
        tmp: int = fast_power(base, exp//2,mod)
        if exp%2==0:
            return tmp * tmp % mod
        else:
            return (tmp * tmp % mod) * (base % mod) % mod
    

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
