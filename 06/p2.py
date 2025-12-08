from collections import deque
from functools import reduce
from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser

class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[str]) -> int:
        ans = 0
        parts = []
        lines = [l + ' ' for l in list(data)]
        ops = deque(lines.pop().split())
        for x in zip(*lines):
            part = "".join(x).strip()
            if part == "":
                ans += sum(parts) if ops.popleft() == "+" else reduce(lambda a,b:a*b, parts)
                parts.clear()
            else:
                parts.append(int(part))

        return ans


if __name__ == '__main__':
    Solution.run(source='input.txt')
