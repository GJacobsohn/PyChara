__author__ = 'gabriel'

from metricvisitor import FunctionMetricVisitor

class McCabeMetric(FunctionMetricVisitor):
    """
    Cyclomatic complexity (or conditional complexity) is a software metric (measurement).
    It was developed by Thomas J. McCabe, Sr. in 1976 and is used to indicate the complexity of a program.
    It directly measures the number of linearly independent paths through a program's source code.
    """

    def __init__(self):
        self._value=1

    def visit_If(self,node):
        self._value+= 1 if len(node.orelse) == 0 else 2
        self.continue_parsing(node)

    def visit_For(self,node):
        self._value+= 1 if len(node.orelse) == 0 else 2
        self.continue_parsing(node)

    def visit_While(self,node):
        self._value+= 1 if len(node.orelse) == 0 else 2
        self.continue_parsing(node)

    def visit_TryExcept(self,node):
        self._value+= len(node.handlers)
        self.continue_parsing(node)

    def visit_TryFinally(self,node):
        self._value+= 1
        self.continue_parsing(node)

    def compute(self):
        value = self._value
        self._value=1
        return value






