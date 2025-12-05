from collections import deque
from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser, IngredientDatabase, IngredientRange


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[IngredientDatabase]) -> int:

        ranges, _ = next(data)
        stack = deque(sorted(ranges, key=lambda r: r._range_start))
        final: list[IngredientRange] = []

        while stack:
            a = stack.popleft()
            if not stack:
                final.append(a)
                break
            b = stack.popleft()
            c = a.join(b)
            if c:
                stack.appendleft(c)
            else:
                final.append(a)
                stack.appendleft(b)
        return sum([x.count() for x in final])


if __name__ == '__main__':
    Solution.run(source='input.txt')
