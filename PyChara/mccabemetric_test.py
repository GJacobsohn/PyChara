__author__ = 'gabriel'

import unittest
from mccabemetric import McCabeMetric
from parser import Parser

class TestMcCabeMetric(unittest.TestCase):

    def setUp(self):
        self.p = None
        self.p = Parser()
        self._metric = McCabeMetric()
        self.p.add_visitor(self._metric)

    def test_simple_file(self):
        self.p.parse_files("test_files/mccabe.py")
        self.assertEqual(self._metric.compute(),9)


if __name__ == '__main__':
    unittest.main()