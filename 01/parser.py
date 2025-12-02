from typing import IO, Iterable, override
from aocfw import IParser


class Parser(IParser):

    @override
    def parse(self, data: IO[str]) -> Iterable[tuple[str, int]]:
        return map(self._parse, data)

    def _parse(self, x: str) -> tuple[str, int]:
        return str(x[0]), int(x[1:].rstrip('\n'))
