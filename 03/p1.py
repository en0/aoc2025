from collections.abc import Iterable
from aocfw import SolutionBase, IParser

from parser import Parser


class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def get_max_battery_index(self, bank: str) -> int:
        val, ret = 0, 0
        for i, battery in enumerate(bank):
            if int(battery) > val:
                ret, val = i, int(battery)
        return ret

    def get_max_joltage(self, bank: str) -> int:
        x = self.get_max_battery_index(bank[:-1])
        y = self.get_max_battery_index(bank[x+1:])
        return int(bank[x] + bank[x+y+1])

    def solve(self, data: Iterable[int]) -> int:
        return sum([self.get_max_joltage(x) for x in data])


if __name__ == '__main__':
    Solution.run(source='input.txt')
