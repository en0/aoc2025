from collections.abc import Iterable
from typing import IO
from aocfw import IParser


class Parser(IParser):
    def parse(self, data: IO[str]) -> Iterable[str]:
        return map(lambda x: str(x).rstrip('\n'), data)
