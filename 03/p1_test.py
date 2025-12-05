from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 357

    def test_get_max_digit_index(self):
        solution = Solution()
        value = "987654321111111"
        x = solution.get_max_battery_index(value[:-1])
        self.assertEqual(x, 0)
        y = solution.get_max_battery_index(value[x+1:])
        self.assertEqual(y, 0)

    def test_get_joltage(self):
        solution = Solution()
        value = "987654321111111"
        x = solution.get_max_joltage(value)
        self.assertEqual(x, 98)


if __name__ == '__main__':
    main()
