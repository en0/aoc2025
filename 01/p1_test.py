from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 3

    def test_example_1(self):
        solution = Solution()
        solution.dial = 11
        _ = solution.solve([
            ('R', 8),
            ('L', 19),
        ])
        self.assertEqual(0, solution.dial)

    def test_example_2(self):
        solution = Solution()
        solution.dial = 5
        _ = solution.solve([
            ('L', 10),
            ('R', 5),
        ])
        self.assertEqual(0, solution.dial)


if __name__ == '__main__':
    main()
