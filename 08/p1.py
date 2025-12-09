from heapq import heappop, heappush
from functools import reduce
from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser, Vec3
from circuit_collection import CircuitCollection
from util import get_distance


class Solution(SolutionBase):

    bindings = {IParser: Parser}
    limit = 1000

    def solve(self, data: Iterable[Vec3]) -> int:

        heap = []
        circuits = CircuitCollection()

        boxes = list(data)
        for i, p in enumerate(boxes):
            circuits.add_circuit({p})
            for j in range(i+1, len(boxes)):
                heappush(heap, (get_distance(p, boxes[j]), p, boxes[j]))

        while heap and self.limit > 0:
            _, box_a, box_b = heappop(heap)
            circuits.connect(box_a, box_b)
            self.limit -= 1

        return reduce(lambda a,b:a*b, circuits.get_counts()[:3])

if __name__ == '__main__':
    Solution.run(source='input.txt')
