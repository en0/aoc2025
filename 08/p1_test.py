from typing import override
from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 40

    @override
    def setUp(self) -> None:
        self.solution.limit = 10
        return super().setUp()


if __name__ == '__main__':
    main()
