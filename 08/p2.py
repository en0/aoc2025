from heapq import heappop, heappush
from collections.abc import Iterable
from aocfw import SolutionBase, IParser
from parser import Parser, Vec3
from circuit_collection import CircuitCollection
from util import Vec3, get_distance

class Solution(SolutionBase):

    bindings = {IParser: Parser}

    def solve(self, data: Iterable[Vec3]) -> int:

        heap = []
        circuits = CircuitCollection()

        boxes = list(data)
        for i, p in enumerate(boxes):
            circuits.add_circuit({p})
            for j in range(i+1, len(boxes)):
                heappush(heap, (get_distance(p, boxes[j]), p, boxes[j]))

        while heap:
            _, box_a, box_b = heappop(heap)
            if circuits.connect(box_a, box_b) == 1:
                return box_a.x * box_b.x

        raise Exception("That didn't work.")

if __name__ == '__main__':
    Solution.run(source='input.txt')
