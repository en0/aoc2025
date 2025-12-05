from collections.abc import Iterable, Iterator
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def get_neighbors(self) -> list["Point"]:
        return [
            Point(self.x-1, self.y - 1),
            Point(self.x,   self.y - 1),
            Point(self.x+1, self.y - 1),
            Point(self.x-1, self.y),
            Point(self.x+1, self.y),
            Point(self.x-1, self.y + 1),
            Point(self.x,   self.y + 1),
            Point(self.x+1, self.y + 1),
        ]


class Grid:

    def __init__(self):
        self._grid: dict[Point, bool] = {}

    def _count_adjacent(self, point: Point) -> int:
        return sum([1 if self._grid.get(p) else 0 for p in point.get_neighbors()])

    def set(self, x: int, y: int):
        self._grid[Point(x, y)] = True

    def unset(self, x: int, y: int):
        self._grid[Point(x, y)] = False

    def get(self, x: int, y: int) -> bool:
        return self._grid.get(Point(x, y), False)

    def collect(self) -> list[tuple[Point, int]]:
        return [(p, self._count_adjacent(p)) for p, v in self._grid.items() if v]

