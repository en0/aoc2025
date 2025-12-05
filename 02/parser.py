from typing import IO, overload
from collections.abc import Iterable
from aocfw import IParser


class Parser(IParser):

    def parse(self, data: IO[str]) -> Iterable[tuple[int, int]]:
        for i in data.readline().split(','):
            a, b = i.split('-')
            yield int(a), int(b)
