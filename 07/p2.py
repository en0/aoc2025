from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[int]) -> int:

        beams: dict[int, int] = {
            x:1 if c == "S" else 0
            for x, c in enumerate(next(data))
        }

        for line in data:
            for x, c in enumerate(line):
                if c == "^" and x in beams:
                    beams[x-1] += beams[x]
                    beams[x+1] += beams[x]
                    beams[x] = 0

        return sum(beams.values())


if __name__ == '__main__':
    Solution.run(source='input.txt')
