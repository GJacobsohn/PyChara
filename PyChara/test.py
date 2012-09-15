from platform import node
from reportlab.lib.validators import isInstanceOf

__author__ = 'gabriel'

from ast import *
from metricvisitor import FunctionMetricVisitor
import ast

class Test (FunctionMetricVisitor):
    def __init__(self):
        self.nodecnt=0

    def compute(self):
        res  = self.nodecnt
        self.nodecnt=0
        return res

    def visit(self, node, stack=None):
        if not stack: stack = []
   #     print stack
        self.generic_visit(node,stack)

    def generic_visit(self, node, stack=None):
        """Called if no explicit visitor function exists for a node."""
        if not stack: stack = []
        for field, value in iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    self.visit(item,stack+ [item])
                    if isinstance(item,FunctionDef):
                        print (str(self.compute()))
            elif isinstance(value, AST):
                self.visit(value,stack)


if __name__ == '__main__':
    with open("test_files/mccabe.py", "r") as source_file:
       Test().visit(ast.parse(source_file.read()))


ClassDef(
    name='testClass',
    bases=[],
    body=[
        FunctionDef(name='ABC', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='feeling', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[If(test=Compare(left=Name(id='feeling', ctx=Load()), ops=[Eq()], comparators=[Str(s='good')]), body=[Print(dest=None, values=[Str(s='HEEELLLLOOO World.')], nl=True)], orelse=[If(test=Compare(left=Name(id='feeling', ctx=Load()), ops=[Eq()], comparators=[Str(s='ok')]), body=[Print(dest=None, values=[Str(s='HELLO WORLD')], nl=True)], orelse=[Print(dest=None, values=[Str(s='bye World')], nl=True)])])], decorator_list=[]),
        FunctionDef(name='feelbarometer', args=arguments(args=[Name(id='self', ctx=Param()), Name(id='feelnumber', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[While(test=Compare(left=Name(id='feelnumber', ctx=Load()), ops=[Gt()], comparators=[Num(n=0)]), body=[AugAssign(target=Name(id='feelnumber', ctx=Store()), op=Sub(), value=Num(n=1))], orelse=[Assign(targets=[Name(id='feelnumber', ctx=Store())], value=Num(n=0))])], decorator_list=[])], decorator_list=[])
