__author__ = 'gabriel'

import unittest
from pychara.metrics.mccabemetric import McCabeMetric
from parser import Parser

class TestMcCabeMetric(unittest.TestCase):

    def setUp(self):
        self.p = None
        self.p = Parser()
        self._metric = McCabeMetric()
        self.p.add_visitor(self._metric)

    def test_simple_file(self):
        self.p.parse_files("test_files/mccabe.py")
        exp_result= dict (
            a=dict(McCabe=8),
            testClass=dict(
                ABC=dict(
                    McCabe=5,
                    av = dict (
                        ab = dict(McCabe=1)
                    )
                ),
                feelbarometer=dict(
                    McCabe=3,
                    bvc = dict (McCabe=1)
                )
            ),
            classy_function=dict(McCabe=2)
        )
        self.assertDictEqual(self._metric._results,exp_result)


if __name__ == '__main__':
    unittest.main()