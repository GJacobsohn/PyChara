__author__ = 'gabriel'

import unittest
from parser import Parser
from pychara.metrics.metricvisitor import MetricVisitor

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

    def test_add_visitor(self):
        """ Adding a real MetricVisitor Object """
        mv = [TestMetric(), TestMetric()]
        self.p.add_visitor(mv[0])
        self.p.add_visitor(mv[1])
        self.assertListEqual(self.p._visitor_list, mv)

    def test_add_visitor_2(self):
        """ Adding a MetricVisitor by String"""
        self.p.add_visitor("McCabeMetric")
        from metrics.mccabemetric import McCabeMetric
        self.assertEqual(self.p._visitor_list[0].metric_name,
                         McCabeMetric().metric_name)

    def test_add_visitor_3(self):
        """ Adding a list of metrics by string """
        self.p.add_visitor(["McCabeMetric","McCabeMetric"])
        from metrics.mccabemetric import McCabeMetric
        self.assertEqual(self.p._visitor_list[0].metric_name,
            McCabeMetric().metric_name)
        self.assertEqual(self.p._visitor_list[1].metric_name,
            McCabeMetric().metric_name)



if __name__ == '__main__':
    unittest.main()
