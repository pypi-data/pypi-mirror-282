
class AbstractBaseGraph():
    def __init__(self, level=0, verbose=False, verbose_prefix='[AbstractBaseGraph]', verbose_indent=' '*2):
        ''' Creates a new graph. '''
        self.level           = level
        self._verbose        = verbose
        self._verbose_prefix = verbose_prefix
        self._verbose_indent = verbose_indent
        # for backward compatibility #TODO remove
        self.verbose        = verbose
        self.verbose_prefix = verbose_prefix

    def __str__(self):
        return str(type(self))

    def _shallowCopy(self, **kwargs):
        return type(self)(level=self.level,
                          verbose=self._verbose,
                          verbose_prefix=self._verbose_prefix,
                          verbose_indent=self._verbose_indent, **kwargs)

    def isValid(self):
        raise NotImplementedError

    def addNode(self, nodeObject):
        raise NotImplementedError

    def addEdge(self, nodeSource, nodeTarget):
        raise NotImplementedError

    def setNodeAttribute(self, node, attributeName, attributeValue):
        raise NotImplementedError

    def setEdgeAttribute(self, edge, attributeName, attributeValue):
        raise NotImplementedError

    def setGraphAttribute(self, attributeName, attributeValue):
        raise NotImplementedError

    def visit(self, controllerGraph, controllerNode, controllerEdge):
        """ Visits every node and edge of the graph. """
        raise NotImplementedError

    def traverse(self, controllerGraph, controllerNode, controllerEdge):
        """ Traverses every node and edge of the graph, beginning from a root
        and respecting dependencies in the graph. """
        raise NotImplementedError

    def print_verbose(self, *args, indentLevel=None, **kwargs):
        if self._verbose:
            if indentLevel is None:
                indentLevel = self.level
            print(self._verbose_prefix + self._verbose_indent * indentLevel, *args, **kwargs)
