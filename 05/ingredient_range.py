class IngredientRange:

    def __init__(self, range_start: int, range_end: int):
        self._range_start: int = range_start
        self._range_end: int = range_end

    def in_range(self, value: int) -> bool:
        return self._range_start <= value <= self._range_end

    def count(self) -> int:
        return self._range_end - self._range_start + 1

    def join(self, other: "IngredientRange") -> "IngredientRange | None":
        rel = [self.in_range(other._range_start), self.in_range(other._range_end)]

        if rel == [True, True]:
            return self

        if rel == [True, False]:
            return IngredientRange(self._range_start, other._range_end)

        if rel == [False, True]:
            return IngredientRange(other._range_start, self._range_end)

        return None
