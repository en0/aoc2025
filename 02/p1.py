from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser


def _digit_count(n: int) -> int:
    return len(str(n))

class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[tuple[int, int]]) -> int:
        total = 0
        for a, b in data:
            n = a
            while n <= b:
                c = _digit_count(n)
                if c % 2 == 0:
                    i = c // 2
                    s = str(n)
                    if s[:i] == s[i:]:
                        total += n
                n += 1
        return total


if __name__ == '__main__':
    Solution.run(source='input.txt')
