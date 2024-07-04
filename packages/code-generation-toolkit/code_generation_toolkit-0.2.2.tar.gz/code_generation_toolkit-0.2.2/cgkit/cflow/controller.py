import enum


class CtrRet(enum.Enum):
    VOID    = -1
    SUCCESS = 0
    ERROR   = 1


class AbstractController():

    def __init__(self, controllerType, verbose=False, verbose_prefix='[AbstractController]'):
        ''' Creates a new controller. '''
        # set options
        self.controllerType = controllerType #TODO check if type is valid
        self.verbose        = verbose
        self.verbose_prefix = verbose_prefix

    def __str__(self):
        """ Returns string of controller. """
        return str(type(self))

    def __call__(self, *args, **kwargs):
        """ Executes controller. """
        raise NotImplementedError

    def q(self, *args, **kwargs):
        """ Finalizes execution of controller (use abbreviation `q` for quit). """
        raise NotImplementedError


class AbstractControllerNode(AbstractController):

    def __init__(self, controllerType, verbose=False, verbose_prefix='[AbstractControllerNode]'):
        ''' Creates a new controller. '''
        super().__init__(controllerType=controllerType, verbose=verbose, verbose_prefix=verbose_prefix)

    def __call__(self, graph, node, nodeAttribute):
        """ Executes controller. """
        raise NotImplementedError

    def q(self, graph, node, nodeAttribute):
        """ Finalizes execution of controller. """
        return CtrRet.SUCCESS


class AbstractControllerEdge(AbstractController):

    def __init__(self, controllerType, verbose=False, verbose_prefix='[AbstractControllerEdge]'):
        ''' Creates a new controller. '''
        super().__init__(controllerType=controllerType, verbose=verbose, verbose_prefix=verbose_prefix)

    def __call__(self, graph, srcNode, srcAttribute, trgNode, trgAttribute, edgeAttribute):
        """ Executes controller. """
        raise NotImplementedError

    def q(self, graph, srcNode, srcAttribute, trgNode, trgAttribute, edgeAttribute):
        """ Finalizes execution of controller. """
        return CtrRet.SUCCESS


class AbstractControllerMultiEdge(AbstractController):

    def __init__(self, controllerType, verbose=False, verbose_prefix='[AbstractControllerMultiEdge]'):
        ''' Creates a new controller. '''
        super().__init__(controllerType=controllerType, verbose=verbose, verbose_prefix=verbose_prefix)

    def __call__(self, graph, node, nodeAttribute, successors):
        """ Executes controller. """
        raise NotImplementedError

    def q(self, graph, node, nodeAttribute, predecessors):
        """ Finalizes execution of controller. """
        return CtrRet.SUCCESS


class AbstractControllerGraph(AbstractController):

    def __init__(self, controllerType, verbose=False, verbose_prefix='[AbstractControllerGraph]'):
        ''' Creates a new controller. '''
        super().__init__(controllerType=controllerType, verbose=verbose, verbose_prefix=verbose_prefix)

    def __call__(self, graph, graphAttribute):
        """ Executes controller. """
        raise NotImplementedError

    def q(self, graph, graphAttribute):
        """ Finalizes execution of controller. """
        return CtrRet.SUCCESS


def controllerIsValid(controller, superclass):
    """ Checks whether the controller belongs to / inherits from the class `superclass`. """
    return issubclass(type(controller), superclass)
