from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[str]) -> int:

        beams: set[int] = set()
        splits: int = 0

        beams.add([x for x, c in enumerate(next(data)) if c == "S"][0])

        for line in data:
            for x, c in enumerate(line):
                if c == "^" and x in beams:
                    splits += 1
                    beams.remove(x)
                    beams.add(x-1)
                    beams.add(x+1)
        return splits


if __name__ == '__main__':
    Solution.run(source='input.txt')
