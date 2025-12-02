from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 6

    def test_example_1(self):
        solution = Solution()
        solution.dial = 50
        ans = solution.solve([
            ('R', 1000),
        ])
        self.assertEqual(50, solution.dial)
        self.assertEqual(10, ans)


if __name__ == '__main__':
    main()
