from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from grid import Grid


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 13


class GridTests(TestCase):

    def setUp(self):
        self.unit: Grid = Grid()

    def test_create_grid(self):
        self.assertIsInstance(self.unit, Grid)

    def test_set_cell(self):
        self.unit.set(0, 0)
        self.assertTrue(self.unit.get(0, 0))

    def test_get_empty_cell(self):
        self.assertFalse(self.unit.get(0, 0))


if __name__ == '__main__':
    main()
