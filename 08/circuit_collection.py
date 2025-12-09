from parser import Vec3


class CircuitCollection:

    def __init__(self) -> None:
        self.circuits: list[set[Vec3]] = []

    def _circuit_of(self, box: Vec3) -> set[Vec3]:
        for c in self.circuits:
            if box in c:
                return c
        raise Exception("What did you do?")

    def add_circuit(self, circuit: set[Vec3]) -> None:
        self.circuits.append(circuit)

    def connect(self, box_a: Vec3, box_b: Vec3) -> int:
        a = self._circuit_of(box_a)
        b = self._circuit_of(box_b)
        if a == b:
            return
        self.circuits.remove(b)
        a.update(b)
        return len(self.circuits)

    def get_counts(self) -> list[int]:
        return sorted([len(p) for p in self.circuits], reverse=True)
