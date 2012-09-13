# coding=utf-8
"""
Interface for Traversing on the Source
"""
import ast

class MetricVisitor(ast.NodeVisitor):

    def continue_parsing(self, node):
        super(MetricVisitor,self).generic_visit(node)


class FunctionMetricVisitor(MetricVisitor):
    """ Computes the Metric function on the and of an Function """

    def compute(self):
        """
        Returns the value of an function based metric for one function

        :rtype: int
        """
        raise NotImplementedError("Must be implemented")