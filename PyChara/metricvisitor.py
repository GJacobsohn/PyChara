# coding=utf-8
"""
Interface for Traversing on the Source
"""
import ast

class MetricVisitor(ast.NodeVisitor):

    def continue_parsing(self, node):
        super(MetricVisitor,self).generic_visit(node)
