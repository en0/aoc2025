from typing import override
from collections.abc import Iterable

from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}
    _value: int = 50

    @override
    def solve(self, data: Iterable[tuple[str, int]]) -> int:
        ans = 0
        for i, (d, v) in enumerate(data):
            self.dial += v if d == "R" else -v
            self.dial %= 100
            ans += 1 if self.dial == 0 else 0
        return ans

    @property
    def dial(self) -> int:
        return self._value

    @dial.setter
    def dial(self, value: int) -> None:
        self._value = value


if __name__ == '__main__':
    Solution.run(source='input.txt')
