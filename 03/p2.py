from typing import override
from aocfw import IParser

from parser import Parser
from p1 import Solution as P1Solution


class Solution(P1Solution):

    bindings = {IParser: Parser}

    @override
    def get_max_joltage(self, bank: str) -> int:
        batteries: list[str] = []
        battery_index = -1
        for i in range(-11, 1, 1):
            bank_slice = bank[battery_index + 1: i] if i < 0 else bank[battery_index + 1:]
            battery_index = self.get_max_battery_index(bank_slice) + battery_index + 1
            batteries.append(bank[battery_index])
        return int("".join(batteries))


if __name__ == '__main__':
    Solution.run(source='input.txt')
