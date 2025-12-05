from collections.abc import Iterable
from typing import IO
from aocfw import IParser
from ingredient_range import IngredientRange


IngredientDatabase = tuple[list[IngredientRange], list[int]]


class Parser(IParser):

    def parse(self, data: IO) -> Iterable[IngredientDatabase]:

        ranges: list[IngredientRange] = []
        ingredients: list[int] = []

        for line in data:
            if line == "\n": break
            start_range, stop_range = [int(x) for x in line.rstrip('\n').split('-', 2)]
            ranges.append(IngredientRange(start_range, stop_range))

        for line in data:
            ingredients.append(int(line))

        yield ranges, ingredients
