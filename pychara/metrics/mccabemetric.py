__author__ = 'gabriel'

from pychara.metrics.metricvisitor import FunctionMetricVisitor

class McCabeMetric(FunctionMetricVisitor):
    """
    Cyclomatic complexity (or conditional complexity) is a software metric (measurement).
    It was developed by Thomas J. McCabe, Sr. in 1976 and is used to indicate the complexity of a program.
    It directly measures the number of linearly independent paths through a program's source code.
    (Wikipedia)
    """
    metric_name='McCabeMetric'

    def __init__(self):
        """ Constructor """
        self._value=1

    def visit_If(self,node,stack):
        """ If new Path, else New Path
            :param node: If Node
            :type node: _ast.Node

            ;param stack; Call stack
            :type node: [_ast.Node]
        """
        self._value+= 1 if len(node.orelse) == 0 else 2


    def visit_For(self,node,stack):
        """ For new Path, 'else' new Path
            :param node: If Node
            :type node: _ast.Node

            ;param stack; Call stack
            :type node: [_ast.Node]
        """
        self._value+= 1 if len(node.orelse) == 0 else 2

    def visit_While(self,node,stack):
        """ While new Path, 'else' new Path
            :param node: If Node
            :type node: _ast.Node

            ;param stack; Call stack
            :type node: [_ast.Node]
        """
        self._value+= 1 if len(node.orelse) == 0 else 2

    def visit_TryExcept(self,node,stack):
        """ For new Path, 'else' new Path
            :param node: TryExcept Node
            :type node: _ast.Node

            ;param stack; Call stack
            :type node: [_ast.Node]
        """
        self._value+= len(node.handlers)

    def compute(self):
        """ Returns the Cyclomatic Value of an Function
            :rtype: int
        """
        value = self._value
        self._value=1
        return value






