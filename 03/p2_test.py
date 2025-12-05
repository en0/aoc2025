from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 3121910778619

    def test_get_joltage(self):
        solution = Solution()
        value = "811111111111119"
        x = solution.get_max_joltage(value)
        self.assertEqual(x, 811111111119)


if __name__ == '__main__':
    main()
