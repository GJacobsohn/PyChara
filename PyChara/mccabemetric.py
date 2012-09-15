__author__ = 'gabriel'

from metricvisitor import FunctionMetricVisitor

class McCabeMetric(FunctionMetricVisitor):
    """
    Cyclomatic complexity (or conditional complexity) is a software metric (measurement).
    It was developed by Thomas J. McCabe, Sr. in 1976 and is used to indicate the complexity of a program.
    It directly measures the number of linearly independent paths through a program's source code.
    """
    metric_name='McCabe'

    def __init__(self):
        self._value=1

    def visit_If(self,node,stack):
        self._value+= 1 if len(node.orelse) == 0 else 2

    def visit_For(self,node,stack):
        self._value+= 1 if len(node.orelse) == 0 else 2

    def visit_While(self,node,stack):
        self._value+= 1 if len(node.orelse) == 0 else 2

    def visit_TryExcept(self,node,stack):
        self._value+= len(node.handlers)

    def compute(self):
        value = self._value
        self._value=1
        return value






