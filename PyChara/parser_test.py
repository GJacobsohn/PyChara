__author__ = 'gabriel'

import unittest
from parser import Parser
from metricvisitor import MetricVisitor

class TestMetric(MetricVisitor):

    def __init__(self):
        self.returns = []

    def visit_FunctionDef(self,node):
        self.returns.append(node.name)
        self.continue_parsing(node)


class TestParser(unittest.TestCase):

    def setUp(self):
        self.p = None
        self.p = Parser()

    def test_simple_file(self):
        test_metric= TestMetric()
        self.p.add_visitor(test_metric)
        self.p.parse_files("test_files/simple.py")
        self.assertListEqual(test_metric.returns,['a','b'])


if __name__ == '__main__':
    unittest.main()
