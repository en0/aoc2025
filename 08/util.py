import math
from typing import NamedTuple


class Vec3(NamedTuple):
    x: int
    y: int
    z: int


def get_distance(a: Vec3, b: Vec3):
    return math.sqrt(sum([
        math.pow(a.x - b.x, 2),
        math.pow(a.y - b.y, 2),
        math.pow(a.z - b.z, 2),
    ]))
