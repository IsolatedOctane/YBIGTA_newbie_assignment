from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        # 구현하세요!
        """
        key: x행 y열
        value: 행렬의 값
        """
        self.matrix[key[0]][key[1]]=value % self.MOD

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        # 구현하세요!
        """
        matrix의 거듭제곱을 계산하는 메소드

        1629에서 풀었던 것 처럼, 분할 정복을 이용한다.

        0: base case

        그외는 홀수와 짝수로 나누어서 계산해보자.

        """
        if n==0:  #identity matrix
            return Matrix.eye(self.shape[0])
        else:
            tmp: Matrix = self.__pow__(n//2)
            if n%2==0:
                return tmp.__matmul__(tmp)
            else:
                return self.__matmul__(tmp.__matmul__(tmp))

    def __repr__(self) -> str:
        # 구현하세요!
        """
        matrix 출력 메소드.

        solution: 리턴 스트링

        """
        solution : str = ""

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                solution+=(str(self.matrix[i][j] % self.MOD)+" ")
            solution+="\n"
        return solution





from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()