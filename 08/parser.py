from collections.abc import Iterable
from typing import IO
from aocfw import IParser
from util import Vec3


class Parser(IParser):
    def parse(self, data: IO[str]) -> Iterable[Vec3]:
        for line in data:
            yield Vec3(*[int(_) for _ in line.rstrip().split(',')])
