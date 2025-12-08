from collections.abc import Iterable
from functools import reduce
from aocfw import SolutionBase, IParser
from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[str]) -> int:

        ans = 0
        problems: list[list[int]] = []

        for part in next(data).split():
            problems.append([int(part)])

        for line in data:
            for i, part in enumerate(line.split()):
                try:
                    value = int(part)
                    problems[i].append(value)

                except ValueError:
                    if part == "*":
                        ans += reduce(lambda a,b:a*b, problems[i])
                    else:
                        ans += sum(problems[i])

        return ans


if __name__ == '__main__':
    Solution.run(source='input.txt')
