from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser


def _is_invalid(n) -> bool:
    limit = len(n)//2
    for i in range(1, limit + 1):
        groups = len(n) // i
        sets = set()
        for j in range(groups):
            sets.add("".join(n[j*i:j*i+i]))
            if len(sets) > 1:
                break
            if j*i+i == len(n):
                return True
    return False


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[tuple[int, int]]) -> int:
        total = 0
        for a, b in data:
            n = a
            while n <= b:
                l = list(str(n))
                if _is_invalid(l):
                    total += n
                n += 1
        return total


if __name__ == '__main__':
    Solution.run(source='input.txt')
