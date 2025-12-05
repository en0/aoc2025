from collections.abc import Iterable
from aocfw import SolutionBase, IParser

from parser import Parser
from grid import Grid


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def build_grid(self, data: Iterable[int]) -> Grid:
        grid = Grid()
        for y, line in enumerate(data):
            for x, content in enumerate(line):
                if content == "@":
                    grid.set(x, y)
        return grid

    def solve(self, data: Iterable[int]) -> int:
        return sum([1 for _, c in self.build_grid(data).collect() if c < 4])


if __name__ == '__main__':
    Solution.run(source='input.txt')
