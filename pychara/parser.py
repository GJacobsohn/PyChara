# coding=utf-8
"""
Parser parses the Python sourcefiles with the given MetricVisitors
"""
__author__ = 'Gabriel Jacobsohn'

from ast import parse
from pychara.metrics.metricvisitor import MetricVisitor
import re
import os


class Parser(object):
    """
    The Parser Class for Parsing a Python sourcefiles
    """

    def __init__(self):
        """
        """
        self._visitor_list= []

    def iter_path(self,path,name="*.py"):
        reg = re.compile("^"+name.replace('.','[.]').replace('*','.*')+"$")
        for root, dirs, files in os.walk(path):
            for curr_file in files:
                if reg.match(curr_file):
                    yield os.path.join(root, curr_file)

    def parse_files(self, path,filename, recursive=False):
        """
        Parses one file with all registered MetricVisitors

        :param path: Where to start the calculations
        :type path: str

        :param filename: Pythonsourcefile that should be Parsed
        :type filename: str

        :param recursive: Search recursive for files
        :type recursive: bool

        :rtype : None
        """
        for file in self.iter_path(path,filename):
            self._module_name = file
            with open(file, "r") as source_file:
                tree = parse(source_file.read())
                for visitor in self._visitor_list:
                    visitor.visit(tree,[])
                    print str(visitor.get_results())
                    visitor._results=dict()


    def add_visitor(self, visitor):
        """
        Add a MetricVisitor to the visitor list for parsing

        :param visitor: Visitor that should be registered
        :type visitor: MetricVisitor
        """
        if isinstance(visitor, MetricVisitor):
            self._visitor_list.append(visitor)
        elif isinstance(visitor,list):
            for v in visitor:
                self.add_visitor(v)
        elif isinstance(visitor,str):
            visitor_module =__import__("pychara.metrics."+str.lower(visitor),fromlist=[str.lower(visitor)])
            class_ = getattr(visitor_module,visitor)
            self.add_visitor(class_())