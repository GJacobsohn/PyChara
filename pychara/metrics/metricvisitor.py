# coding=utf-8
"""
Interface for Traversing on the Source
"""
import ast
from ast import iter_fields

class MetricVisitor():

    def get_results(self):
        if getattr(self,'_results',None) is None:
            self._results = dict()
        return self._results

    def save_value(self,value,stack):
        """
        Saves the Result from an run.

        :param value:
        :ptype value: int


        """
        results = self.get_results()
        for node in stack:
            if results.has_key(node.name):
                results = results[node.name]
            else:
                results[node.name] = dict()
                results =results[node.name]
        results[self.metric_name]=value




class FunctionMetricVisitor(MetricVisitor):
    """ Computes the Metric function on the and of an Function """

    def compute(self):
        """
        Returns the value of an function based metric for one function

        :rtype: int
        """
        raise NotImplementedError("Must be implemented")

    def visit(self, node):
        """Visit a node."""
        self.visit(node,[])

    def generic_visit(self,node,stack):
        pass

    def _visit_node_calc(self,node,stack):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        visitor(node,stack)

    def visit(self, node, stack):
        for field, value in iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    self._visit_node_calc(item,stack+ [item])
                    self.visit(item,stack+ [item])
                    if isinstance(item,ast.FunctionDef):
                        self.save_value(self.compute(),stack+[item])
            elif isinstance(value, ast.AST):
                self._visit_node_calc(value,stack+[value])
                self.visit(value,stack+[value])
