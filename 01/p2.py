from typing import override
from collections.abc import Iterable

from aocfw import IParser
from parser import Parser
from p1 import Solution as SolutionP1


class Solution(SolutionP1):

    bindings = {IParser: Parser}
    _value: int = 50

    @override
    def solve(self, data: Iterable[tuple[str, int]]) -> int:
        ans = 0
        for i, (d, v) in enumerate(data):
            ans += v // 100
            _dial = self.dial
            self.dial += v if d == "R" else -v
            self.dial %= 100
            if self.dial == 0:
                ans += 1
            elif _dial > 0 and d == 'R' and self.dial < _dial:
                ans += 1
            elif _dial > 0 and d == 'L' and self.dial > _dial:
                ans += 1
        return ans


if __name__ == '__main__':
    Solution.run(source='input.txt')
