#####################
# Nodes of Task Graph
#####################

class AbstractNode():
    def __init__(self, nodeType='Abstract'):
        self.type = nodeType

    def __str__(self):
        return str(self.__class__) + ': ' + str(self.__dict__)


class RootNode(AbstractNode):
    def __init__(self, **kwargs):
        kwargs.setdefault('nodeType', 'Root')
        super().__init__(**kwargs)


class LeafNode(AbstractNode):
    def __init__(self, **kwargs):
        kwargs.setdefault('nodeType', 'Leaf')
        super().__init__(**kwargs)


class PlainCodeNode(AbstractNode):
    def __init__(self, **kwargs):
        kwargs.setdefault('nodeType', 'PlainCode')
        super().__init__(**kwargs)


class WorkNode(AbstractNode):
    def __init__(self, name : str, args=None, ret=None, **kwargs):
        kwargs.setdefault('nodeType', 'Work')
        super().__init__(**kwargs)
        # arg: name
        assert isinstance(name, str), type(name)
        self.name = name
        # arg: args
        if args is None:              self.args = list()
        elif isinstance(args, list):  self.args = args
        else:                         raise TypeError('Cannot handle type {}'.format(type(args)))
        # arg: ret
        if ret is None:               self.ret = list()
        elif isinstance(ret, list):   self.ret = ret
        else:                         raise TypeError('Cannot handle type {}'.format(type(ret)))


class WorkSequenceNode(AbstractNode):
    def __init__(self, workSeq : list, **kwargs):
        kwargs.setdefault('nodeType', 'WorkSequence')
        super().__init__(**kwargs)
        assert isinstance(workSeq, list), type(workSeq)
        self.workSeq = workSeq


class ClusterBeginNode(AbstractNode):
    def __init__(self, clusterEndNode=None, **kwargs):
        kwargs.setdefault('nodeType', 'ClusterBegin')
        super().__init__(**kwargs)
        self.endNode = list()
        if clusterEndNode is not None:
            self.appendEndNode(clusterEndNode)
            clusterEndNode.setBeginNode(self)

    def appendEndNode(self, clusterEndNode):
        assert issubclass(type(clusterEndNode), ClusterEndNode), type(clusterEndNode)
        self.endNode.append(clusterEndNode)

    def hasEndNode(self, clusterEndNode):
        assert issubclass(type(clusterEndNode), ClusterEndNode), type(clusterEndNode)
        return any([clusterEndNode is node for node in self.endNode])

    def hasAllEndNodes(self, clusterEndNode):
        assert isinstance(clusterEndNode, list) or \
               isinstance(clusterEndNode, set), type(clusterEndNode)
        checkResult = [False]*len(clusterEndNode)
        for i, checkNode in enumerate(clusterEndNode):
            if any([checkNode is node for node in self.endNode]):
                checkResult[i] = True
        return all(checkResult)

    def nEndNodes(self):
        return len(self.endNode)


class ClusterEndNode(AbstractNode):
    def __init__(self, clusterBeginNode=None, **kwargs):
        kwargs.setdefault('nodeType', 'ClusterEnd')
        super().__init__(**kwargs)
        if clusterBeginNode is not None:
            self.setBeginNode(clusterBeginNode)
            clusterBeginNode.appendEndNode(self)

    def getBeginNode(self):
        return self.beginNode

    def setBeginNode(self, clusterBeginNode):
        assert issubclass(type(clusterBeginNode), ClusterBeginNode), type(clusterBeginNode)
        self.beginNode = clusterBeginNode

    def hasBeginNode(self, clusterBeginNode):
        assert issubclass(type(clusterBeginNode), ClusterBeginNode), type(clusterBeginNode)
        return clusterBeginNode is self.beginNode


class WorkBeginNode(ClusterBeginNode):
    def __init__(self, workSeq=None, **kwargs):
        kwargs.setdefault('nodeType', 'WorkBegin')
        super().__init__(**kwargs)
        assert workSeq is None or isinstance(workSeq, list), type(workSeq)
        self.workSeq = workSeq


class WorkEndNode(ClusterEndNode):
    def __init__(self, workSeq=None, workBeginNode=None, **kwargs):
        kwargs.setdefault('nodeType', 'WorkEnd')
        kwargs.setdefault('clusterBeginNode', workBeginNode)
        super().__init__(**kwargs)
        assert workSeq is None or isinstance(workSeq, list), type(workSeq)
        self.workSeq = workSeq


#TODO deprecated
#class ActionNode(AbstractNode):
#####DEV
#    from cgkit.ctree.assembler import CodeAssembler
#    import pathlib
#    _codePath = pathlib.Path('.')
#    _codeData = CodeAssembler.load(_codePath / 'ex_sedov_data_Default.json')
#####DEV
#
#    def __init__(self, name : str, args=list()):
#        super().__init__(nodeType='Action')
#        assert isinstance(name, str), type(name)
#        assert isinstance(args, list), type(args)
#        self.name = name
#        self.args = args
#####DEV
#        #assert all([('_param:{}'.format(a) in self._codeData) for a in self.args])
#####DEV
#
#    def assembleCode(self, codeAssembler, device=None):
#        # create function code
#        fnArgs = ['_param:{}'.format(a) for a in self.args]
#        if device is not None:
#            name = '{}_{}'.format(self.name, device)
#        else:
#            name = '{}'.format(self.name)
#        fnCode = [name + '(' + ', '.join(fnArgs) + ');']
#        fnConnector = { '_connector:execute': {'_code': fnCode} }
#        # embed function code into a kernel
#####DEV
#        assert isinstance(device, str), type(device)
#        assert codeAssembler.device == device
#        path_kernel = self._codePath / ('ex_sedov_subroutine_' + device + '_action_kernel.json')
#####DEV
#        tree_kernel = codeAssembler.load(path_kernel)
#        codeAssembler.link_trees(tree_kernel['_connector:execute'], fnConnector)
#        # setup arguments
#        argsCode = list()
#        for a in self.args:
#            s = '_param:setup_{}'.format(a)
#            if s in tree_kernel['_connector:execute']:
#                c = tree_kernel['_connector:execute'][s]
#                if isinstance(c, str):
#                    argsCode.append(c)
#                elif isinstance(c, list):
#                    argsCode.extend(c)
#                else:
#                    raise TypeError('Expected str or list, but got {}'.format(type(c)))
#        if argsCode:
#            argsConnector = { '_connector:setup': {'_code': argsCode} }
#            codeAssembler.link_trees(tree_kernel['_connector:execute'], argsConnector)
#        # embed kernel into a loop
#        if 'CPU' == device:
#            tree = tree_kernel
#        if 'GPU' == device:
#####DEV
#            path_loop = self._codePath / ('ex_sedov_subroutine_' + device + '_action_loop.json')
#####DEV
#            tree_loop = codeAssembler.load(path_loop)
#            codeAssembler.link_trees(tree_loop['_connector:execute'], tree_kernel)
#            tree = tree_loop
#        # link function code into code tree
#        locations = codeAssembler.link(tree, codeAssembler.linkLocation)
#        if not locations:
#            cl = self.__class__.__name__
#            fn = 'assembleCode'
#            codeAssembler.dump(tree, '_debug_{}_{}.json'.format(cl, fn))
#        assert locations, 'Linking failed, using link location: ' + str(codeAssembler.linkLocation)
