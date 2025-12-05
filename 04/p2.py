from collections.abc import Iterable
from aocfw import IParser

from parser import Parser
from p1 import Solution as P1Solution
from grid import Grid


class Solution(P1Solution):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[int]) -> int:
        grid = self.build_grid(data)
        total, step_total = 0, -1
        while not step_total == 0:
            step_total = 0
            for (x, y), c in grid.collect():
                if c < 4:
                    grid.unset(x, y)
                    step_total += 1
            total += step_total
        return total


if __name__ == '__main__':
    Solution.run(source='input.txt')
