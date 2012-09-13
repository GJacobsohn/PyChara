# coding=utf-8
"""
Parser parses the Python sourcefiles with the given MetricVisitors
"""
__author__ = 'Gabriel Jacobsohn'

from ast import parse
from metricvisitor import MetricVisitor

class Parser(object):
    """
    The Parser Class for Parsing a Python sourcefiles
    """

    def __init__(self):
        """
        """
        self._visitor_list= []


    def parse_files(self, filename):
        """
        Parses one file with all registered MetricVisitors

        :param filename: Pythonsourcefile that should be Parsed
        :type filename: str

        :rtype : None
        """
        self._module_name = filename
        with open(filename, "r") as source_file:
            tree = parse(source_file.read())

        for visitor in self._visitor_list:
            visitor.visit(tree)


    def add_visitor(self, visitor):
        """
        Add a MetricVisitor to the visitor list for parsing

        :param visitor: Visitor that should be registered
        :type visitor: MetricVisitor
        """
        if isinstance(visitor, MetricVisitor):
            self._visitor_list.append(visitor)