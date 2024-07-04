'''
Defines the ControlFlowGraph.

TODO
n/a
'''

from cgkit.cflow.basegraph_networkx import BaseGraphNetworkX
from cgkit.cflow.node import RootNode


class ControlFlowGraph(BaseGraphNetworkX):
    deviceDefault = 'Default'

    def __init__(self, initGraph=True, **kwargs):
        ''' Creates a new graph. '''
        # call constructor of super-class
        kwargs.setdefault('verbose_prefix', '[ControlFlowGraph]')
        super().__init__(**kwargs)
        # initialize graph
        if initGraph: self._initGraph()

    def _shallowCopy(self):
        shallowCopy = super()._shallowCopy(initGraph=False)
       #copyAttr = ['memoryName', 'memoryCopy', 'memoryScratch']
       #for name in copyAttr:
       #    setattr(shallowCopy, name, getattr(self, name))
        return shallowCopy

    def _initGraph(self):
        self.addNode(RootNode())
        #TODO root node does not get initialized with any controller

    #-----------
    # Parse Code
    #-----------

    def parseCode(self, controllerGraph=None, controllerNode=None, controllerEdge=None, controllerMultiEdge=None):
        if self.verbose: print(self.verbose_prefix, '<parseCode>')
        self.traverseHierarchy(controllerGraph=controllerGraph,
                               controllerNode=controllerNode,
                               controllerEdge=controllerEdge,
                               controllerMultiEdge=controllerMultiEdge)
        if self.verbose: print(self.verbose_prefix, '</parseCode>')
        return

    #-----------
    # TODO deprecated
    #-----------

    def setNodeDevice(self, node, device : str):
        #TODO deprecated
        assert device in self.deviceList, device
        return self.setNodeAttribute(node, self.deviceName, device)

    def setUp(self):
        self._setUpEdgesRecurively(node=self.root, memoryCopy=list(), memoryScratch=list())
        return

    def _setUpEdgesRecurively(self, node : int, memoryCopy : list, memoryScratch : list):
        '''
            node            Current node
            memoryCopy      Memory to copy for action corresponding to current and adjacent nodes
            memoryScratch   Scratch memory required for current and adjacent nodes
        '''
        from cgkit.cflow.node import ConcurrentDataBeginNode
        assert isinstance(node, int), type(node)
        assert isinstance(memoryCopy, list), type(memoryCopy)
        assert isinstance(memoryScratch, list), type(memoryScratch)
        # process (current) node
        if self.deviceName not in self.G.nodes[node]:  # if device is not set
            self.G.nodes[node][self.deviceName] = self.deviceDefault
        assert 'obj' in self.G.nodes[node]
        if isinstance(self.G.nodes[node]['obj'], ConcurrentDataBeginNode):  # if has memory information
            memoryCopy.extend(self.G.nodes[node]['obj'].Uin)
            memoryScratch.extend(self.G.nodes[node]['obj'].scratch)
        # check the node's neighbors
        for nbr in list(self.G.successors(node)):  # loop over all neighbors
            # process neighboring node
            if self.deviceName not in self.G.nodes[nbr]:  # if device is not set
                self.G.nodes[nbr][self.deviceName] = self.deviceDefault
            isChange = self.G[node][nbr][self.deviceChangeName] = \
                self.nodeAttributeChange(node, nbr, self.deviceName)
            # set edge attributes pertaining to device change
            if isChange:
                self.G[node][nbr][self.deviceSourceName] = self.G.nodes[node][self.deviceName]
                self.G[node][nbr][self.deviceTargetName] = self.G.nodes[nbr][self.deviceName]
                self.G[node][nbr][self.memoryCopy]       = memoryCopy
                self.G[node][nbr][self.memoryScratch]    = memoryScratch
            # recurse into neighboring node
            self._setUpEdgesRecurively(nbr, memoryCopy, memoryScratch)
        return

#TODO deprecated
#   def toPrunedGraph(self):
#       return super().toPrunedGraph(self.deviceChangeName)

#TODO deprecated
#   def toHierarchicalGraph(self):
#       return super().toHierarchicalGraph(self.deviceChangeName)

#TODO deprecated
#   def parseCode(self):
#       # TODO revise use of CodeModelClass
#       assert 'CodeModelClass' in self.G.graph
#       assert self.codeAssembler is not None
#       self.codeAssembler.initializeDriver()
#       codeModel      = self.G.graph['CodeModelClass'](self.codeAssembler)
#       subroutineCode = ControlFlowGraph._parseCodeRecursively_nxGraph(self.G, self.root, codeModel)
#       driverCode     = self.codeAssembler.parse()
#       return driverCode, subroutineCode

    @staticmethod
    def _parseCodeRecursively_nxGraph(nxGraph, node : int, codeModel, isFirst=True, action=list(), subroutine=dict()):
        assert isinstance(node, int), type(node)
        assert isinstance(subroutine, dict), type(subroutine)
        # set unique id
        assert 'device' in nxGraph.nodes[node]
        uId = 'id{}_{}'.format(node, nxGraph.nodes[node]['device'])
        # process (current) node
        assert 'obj' in nxGraph.nodes[node]
        subGraph       = nxGraph.nodes[node]['obj']
        subRoutineName = 'subroutine_{}'.format(uId)
        subCode        = ControlFlowGraph._parseCode_subgraph(subGraph, subRoutineName, codeModel.copyCodeAssembler())
        if subCode:
            subroutine[subRoutineName] = subCode
            actionName = codeModel.assembleCode_setup(uId, 'name DEV',
                                                      nodeAttributes=nxGraph.nodes[node], subRoutineName=subRoutineName)
            #TODO substitute DEV
            if actionName:
                action.append(actionName)
        # go to the node's neighbors
        for nbr in list(nxGraph.successors(node)):  # loop over all neighbors
            ControlFlowGraph._parseCodeRecursively_nxGraph(nxGraph, nbr, codeModel, isFirst=False, action=action, subroutine=subroutine)
        # finalize and return
        if isFirst:
            codeModel.assembleCode_execute('uniqueIdDEV', 'name DEV', action=action)
            #TODO substitute DEV
            return subroutine
        else:
            return None

    @staticmethod
    def _parseCode_subgraph(subGraph, subRoutineName, codeAssembler):
        assert isinstance(subRoutineName, str), type(subRoutineName)
        rootid = BaseGraphNetworkX._searchBounds(subGraph)[0]
        assert 'device' in subGraph.nodes[rootid]
        device = subGraph.nodes[rootid]['device']
        if device != ControlFlowGraph.deviceDefault:
            codeAssembler.initializeSubroutine(functionName=subRoutineName, device=device)
            ControlFlowGraph._parseCodeRecursively_subgraph(subGraph, rootid, codeAssembler)
            return codeAssembler.parse()
        else:
            return None

    @staticmethod
    def _parseCodeRecursively_subgraph(subGraph, node, codeAssembler):
        assert 'obj' in subGraph.nodes[node]
        assert 'device' in subGraph.nodes[node]
        # process (current) node
        device = subGraph.nodes[node]['device']
        subGraph.nodes[node]['obj'].assembleCode(codeAssembler, device=device)
        # go to the node's neighbors
        for nbr in list(subGraph.successors(node)):  # loop over all neighbors
            ControlFlowGraph._parseCodeRecursively_subgraph(subGraph, nbr, codeAssembler)
