from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser, IngredientDatabase, IngredientRange


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[IngredientDatabase]) -> int:
        total = 0
        ranges, ingredients = next(data)
        for ingredient in ingredients:
            if any([range.in_range(ingredient) for range in ranges]):
                total += 1
        return total


if __name__ == '__main__':
    Solution.run(source='input.txt')
