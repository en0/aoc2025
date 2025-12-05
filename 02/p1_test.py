from io import StringIO
from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 1227775554


class SolutionParser(TestCase, TestCaseMixin):

    solution = Solution
    sample = StringIO("1-2,3-4")

    def test_parser(self):
        data = self.get_parsed_data()
        self.assertListEqual(list(data), [(1, 2), (3, 4)])

if __name__ == '__main__':
    main()
