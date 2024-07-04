'''
TODO
- implement checks for return value of calls to controllers
'''

from cgkit.cflow.basegraph import AbstractBaseGraph
from cgkit.cflow.controller import (AbstractControllerNode, AbstractControllerEdge, AbstractControllerMultiEdge, AbstractControllerGraph)
from cgkit.cflow.controller import (CtrRet, controllerIsValid)
from cgkit.cflow.node import (ClusterBeginNode, ClusterEndNode)
import networkx
import numpy


class ControllerNode_TraverseHierarchy(AbstractControllerNode):
    ''' Private controller to parse code at any node. '''

    def __init__(self, controllerGraph, controllerNode, controllerEdge, controllerMultiEdge, verbose, verbose_prefix):
        super().__init__(controllerType='view', verbose=verbose, verbose_prefix=verbose_prefix)
        self.controllerGraph     = controllerGraph
        self.controllerNode      = controllerNode
        self.controllerEdge      = controllerEdge
        self.controllerMultiEdge = controllerMultiEdge

    def __call__(self, graph, node, nodeAttribute):
        if graph.nodeHasSubgraph(node):
            # traverse subgraph
            sGraph = graph.nodeGetSubgraph(node)
           #if self.verbose: print(self.verbose_prefix, '<ControllerNode_TraverseHierarchy subgraph_level={}>'.format(sGraph.level))
            sGraph.traverse(controllerGraph=self.controllerGraph, controllerNode=self,
                            controllerEdge=self.controllerEdge, controllerMultiEdge=self.controllerMultiEdge)
           #if self.verbose: print(self.verbose_prefix, '</ControllerNode_TraverseHierarchy>')
        else:
            # call controller for node
            if self.controllerNode is not None:
                self.controllerNode  (graph, node, nodeAttribute)
                self.controllerNode.q(graph, node, nodeAttribute)
        return CtrRet.SUCCESS


class ControllerEdge_DetectClusters(AbstractControllerEdge):

    def __init__(self, verbose, verbose_prefix):
        super().__init__(controllerType='view', verbose=verbose, verbose_prefix=verbose_prefix)
        # variables for tracking
        self.beginNode    = set()
        self.beginObj     = dict()
        self.endNode      = dict()
        self.endObj       = dict()
        # main variable gathering results
        self.clusterEdges = set()

    def __call__(self, graph, srcNode, srcAttribute, trgNode, trgAttribute, edgeAttribute):
        ''' Adds the given edge to `self.clusterEdges` if it belongs to a cluster.

            We detect a `ClusterBeginNode` and wait until visiting one
            corresponding `ClusterEndNode`.  Having found all end nodes, we
            find all simple paths between the (unique) begin and all its end
            nodes.
        '''
        srcObj = srcAttribute['obj']
        trgObj = trgAttribute['obj']
        # activate collection of edges belonging to cluster
        if issubclass(type(srcObj), ClusterBeginNode):
            assert not srcNode in self.beginNode
            assert not srcNode in self.beginObj
            assert not srcNode in self.endNode
            assert not srcNode in self.endObj
            self.beginNode.add(srcNode)
            self.beginObj[srcNode] = srcObj
            self.endNode[srcNode]  = list()
            self.endObj[srcNode]   = list()
        # deactivate collection of edges
        if issubclass(type(trgObj), ClusterEndNode):
            ob = trgObj.getBeginNode()
            ub = self.getBeginNodeId(ob)
            if ub is not None: # if end node complements a begin node
                self.endNode[ub].append(trgNode)
                self.endObj[ub].append(trgObj)
                if ob.hasAllEndNodes(self.endObj[ub]): # if all end nodes were visited
                    # find all nodes of the cluster
                    for ue in self.endNode[ub]:
                        simplePaths = networkx.all_simple_edge_paths(graph.G, ub, ue)
                        edgesPaths  = set(e for path in simplePaths for e in path)
                        self.clusterEdges = self.clusterEdges.union(edgesPaths)
                    # reset begin/end variables
                    self.beginNode.remove(ub)
                    self.beginObj.pop(ub)
                    self.endNode.pop(ub)
                    self.endObj.pop(ub)
        return CtrRet.SUCCESS

    def getBeginNodeId(self, ob):
        assert issubclass(type(ob), ClusterBeginNode)
        for ub in self.beginNode:
            if ob is self.beginObj[ub]:
                return ub
        return None


class ControllerNode_CreateSubSubgraph(AbstractControllerNode):
    def __init__(self, controllerMarkEdge, controllerInitSubgraph, verbose, verbose_prefix):
        super().__init__(controllerType='modify', verbose=verbose, verbose_prefix=verbose_prefix)
        self.controllerMarkEdge     = controllerMarkEdge
        self.controllerInitSubgraph = controllerInitSubgraph

    def __call__(self, graph, node, nodeAttribute):
        crtret = CtrRet.VOID
        if graph.nodeHasSubgraph(node):
            sGraph = graph.nodeGetSubgraph(node)
            if self.verbose: print(self.verbose_prefix, '<ControllerNode_CreateSubSubgraph subgraph_level={}>'.format(sGraph.level))
            S = sGraph.G
            clusterEdges = sGraph._getClusterEdges(S, self.controllerMarkEdge)
            clusterNodes = sGraph._getClusterNodes(S, clusterEdges)
            H = sGraph._createTwoLevelGraph(S, clusterNodes, 'clusterMarkEdge', controllerInitSubgraph=self.controllerInitSubgraph)
            if H is not None:
                H.graph.update(S.graph)  # keep attributes of previous graph
                hGraph = sGraph._shallowCopy()
                hGraph._setGraph(H, H.number_of_nodes() + 1)
                graph.nodeSetSubgraph(node, hGraph)
                crtret = CtrRet.SUCCESS
            if self.verbose: print(self.verbose_prefix, '</ControllerNode_CreateSubSubgraph>')
        return crtret


class BaseGraphNetworkX(AbstractBaseGraph):
    def __init__(self, **kwargs):
        ''' Creates a new graph. '''
        # call constructor of super-class
        kwargs.setdefault('verbose_prefix', '[BaseGraphNetworkX]')
        super().__init__(**kwargs)
        # initialize node id's
        self._nodeid = 0          # counter for node id's
        self.root = self._nodeid  # id of (unique) root node
        self.leaf = None          # id of (unique) leaf node

    def __str__(self):
        assert hasattr(self, 'G')
        return str(type(self)) + ': Nodes = ' + str(self.G.nodes)

    def _setGraph(self, nxGraph : networkx.DiGraph, nodeid=None):
        assert not hasattr(self, 'G')
        assert isinstance(nxGraph, networkx.DiGraph), type(nxGraph)
        assert nodeid is None or isinstance(nodeid, int), type(nodeid)
        self.G = nxGraph
        if nodeid is not None:
            self._nodeid = nodeid
            self.leaf    = None
        else:
            bounds = self._searchBounds(self.G)
            self.root = bounds[0]
            self.leaf = bounds[1]
            self._nodeid = self.leaf + 1
        return self._nodeid

    @staticmethod
    def _searchBounds(nxGraph):
        lPath = networkx.dag_longest_path(nxGraph)
        return (lPath[0], lPath[-1])

    def getBounds(self):
        assert hasattr(self, 'G')
        if self.leaf is None:  # if need to search leaf id
            bounds = self._searchBounds(self.G)
            assert self.root == bounds[0], (self.root, bounds[0])
            self.leaf = bounds[1]
        return (self.root, self.leaf)

    @staticmethod
    def _isValid_nxGraph(nxGraph, rootidRef=None):
        # check if graph is a DAG
        if not networkx.is_directed_acyclic_graph(nxGraph):
            return False
        # check if graph starts at root
        bounds = BaseGraphNetworkX._searchBounds(nxGraph)
        if rootidRef is not None and not (rootidRef == bounds[0]):
            return False
        # check if all nodes are on a path between root and end nodes
        simplePaths = networkx.all_simple_paths(nxGraph, bounds[0], bounds[1])
        nodesPaths  = set(u for path in simplePaths for u in path)
        nodesGraph  = set(nxGraph.nodes)
        return (nodesPaths == nodesGraph)

    def isValid(self):
        ''' Checks if graph is valid.  This implies that
            - the graph is a directed acyclic graph
            - the graph begins at one and only one node with id == root
            - the graph ends at one and only one node
            - all nodes of the graph are on a path between root and end nodes
        '''
        # check if graph exists
        if not hasattr(self, 'G'):
            return False
        # check if NetworkX graph is valid
        return self._isValid_nxGraph(self.G, self.root)

    def addNode(self, nodeObject):
        # init graph
        if not hasattr(self, 'G'):
            self.G = networkx.DiGraph()
        # update node id / counter
        i = self._nodeid
        self._nodeid += 1
        # deactivate leaf id (each time a new node is added)
        self.leaf = None
        # add node
        if self.verbose:
            print(self.verbose_prefix, 'Add node: {},'.format(i), nodeObject)
        self.G.add_node(i, obj=nodeObject)
        return i

    def addEdge(self, nodeSource : int, nodeTarget : int):
        assert isinstance(nodeSource, int) or nodeSource is None, type(nodeSource)
        assert isinstance(nodeTarget, int), type(nodeTarget)
        if nodeSource is None:
            nodeSource = self.root
        if self.verbose:
            print(self.verbose_prefix, 'Add edge:', nodeSource, '->', nodeTarget)
        self.G.add_edge(nodeSource, nodeTarget)
        return (nodeSource, nodeTarget)

    def setNodeAttribute(self, node, attributeName : str, attributeValue):
        assert isinstance(attributeName, str), type(attributeName)
        try:
            for u in node:
                assert isinstance(u, int), type(u)
                self.G.nodes[u][attributeName] = attributeValue
        except TypeError:
            assert isinstance(node, int), type(node)
            self.G.nodes[node][attributeName] = attributeValue
        except:
            raise
        return

    def setEdgeAttribute(self, edge, attributeName : str, attributeValue):
        assert isinstance(attributeName, str), type(attributeName)
        try:
            self.G.edges[edge][attributeName] = attributeValue
        except ValueError:
            for e in edge:
                assert isinstance(e, tuple), type(e)
                self.G.edges[e][attributeName] = attributeValue
        except:
            raise
        return

    def setGraphAttribute(self, attributeName, attributeValue):
        assert isinstance(attributeName, str), type(attributeName)
        self.G.graph[attributeName] = attributeValue
        return

    def linkNode(self, nodeObject, controllerNode=None, controllerEdge=None):
        assert nodeObject is not None
        assert controllerNode is None or controllerIsValid(controllerNode, AbstractControllerNode)
        assert controllerEdge is None or controllerIsValid(controllerEdge, AbstractControllerEdge)
        def link_fn(sourceNode):
            """ depends on `nodeObject` """
            assert sourceNode is not None
            nodeid = self.addNode(nodeObject)
            if controllerNode is not None:
                controllerNode(self, nodeid, self.G.nodes[nodeid])
            try:
                for s in sourceNode:
                    self.addEdge(s, nodeid)
                    if controllerEdge is not None:
                        controllerEdge(self, s, self.G.nodes[s]. nodeid, self.G.nodes[nodeid], self.G[s][nodeid])
            except TypeError:
                assert isinstance(sourceNode, int), type(sourceNode)
                self.addEdge(sourceNode, nodeid)
                if controllerEdge is not None:
                    controllerEdge(self, s, self.G.nodes[s]. nodeid, self.G.nodes[nodeid], self.G[s][nodeid])
            except:
                raise
            return nodeid
        return link_fn

    #-------------------------
    # Visit and Traverse Graph
    #-------------------------

    def visit(self, controllerGraph=None, controllerNode=None, controllerEdge=None):
        if self.verbose:
            print(self.verbose_prefix, '<visit controllerGraph={}, controllerNode={}, controllerEdge={}>'.format(
                    controllerGraph is not None, controllerNode is not None, controllerEdge is not None
            ))
        assert controllerGraph is None or controllerIsValid(controllerGraph, AbstractControllerGraph)
        assert controllerNode  is None or controllerIsValid(controllerNode , AbstractControllerNode )
        assert controllerEdge  is None or controllerIsValid(controllerEdge , AbstractControllerEdge )
        # call controller for graph
        if controllerGraph is not None:
            if self.verbose: print(self.verbose_prefix, '  <visit_controllerGraph>')
            controllerGraph(self, self.G.graph)
        # visit every node and edge
        for u, adjdict in self.G.adjacency():  # loop over all nodes
            if controllerNode is not None:
                if self.verbose: print(self.verbose_prefix, '  <visit_controllerNode node={} />'.format(u))
                controllerNode  (self, u, self.G.nodes[u])
                controllerNode.q(self, u, self.G.nodes[u])
            if controllerEdge is not None:
                for v, eattr in adjdict.items():  # loop over all neighbors
                    if self.verbose: print(self.verbose_prefix, '<visit_controllerEdge src={}, trg={} />'.format(u,v))
                    controllerEdge  (self, u, self.G.nodes[u], v, self.G.nodes[v], self.G[u][v])
                    controllerEdge.q(self, u, self.G.nodes[u], v, self.G.nodes[v], self.G[u][v])
        # finalize controller for graph
        if controllerGraph is not None:
            controllerGraph.q(self, self.G.graph)
            if self.verbose: print(self.verbose_prefix, '  </visit_controllerGraph>')
        if self.verbose: print(self.verbose_prefix, '</visit>')
        return

    def traverseRecursively(self, controllerGraph=None, controllerNode=None, controllerEdge=None):
        if self.verbose:
            print(self.verbose_prefix, '<traverseRecursively controllerGraph={}, controllerNode={}, controllerEdge={}>'.format(
                    controllerGraph is not None, controllerNode is not None, controllerEdge is not None
            ))
        assert controllerGraph is None or controllerIsValid(controllerGraph, AbstractControllerGraph)
        assert controllerNode  is None or controllerIsValid(controllerNode , AbstractControllerNode )
        assert controllerEdge  is None or controllerIsValid(controllerEdge , AbstractControllerEdge )
        # call controller for graph
        if controllerGraph is not None:
            if self.verbose: print(self.verbose_prefix, '<traverseRecursively_controllerGraph>')
            controllerGraph(self, self.G.graph)
        # traverse graph beginning at the root
        ret = self._traverseRecursively(self.root,
                                        controllerNode=controllerNode,
                                        controllerEdge=controllerEdge)
        # finalize controller for graph
        if controllerGraph is not None:
            controllerGraph.q(self, self.G.graph)
            if self.verbose: print(self.verbose_prefix, '</traverseRecursively_controllerGraph>')
        if self.verbose: print(self.verbose_prefix, '</traverseRecursively>')
        return ret

    def _traverseRecursively(self, node, controllerNode=None, controllerEdge=None):
        # check if node has been visited by all of its predecessors
        nPredecessors = self.G.in_degree(node)
        if 1 < nPredecessors:
            if '_traverse_n_visited' in self.G.nodes[node]:  # if has been visited once or more
                nVisited = self.G.nodes[node]['_traverse_n_visited']
                if nVisited < (nPredecessors - 1):
                    self.G.nodes[node]['_traverse_n_visited'] += 1
                    return  # skip because node has not been visited by all predecessors yet
                else:
                    self.G.nodes[node].pop('_traverse_n_visited')
            else:  # otherwise node has never been visited
                self.G.nodes[node]['_traverse_n_visited'] = 1
                return  # skip because node has not been visited by all predecessors yet
        # call controller for this node
        if controllerNode is not None:
            if self.verbose: print(self.verbose_prefix, '  <traverseRecursively_controllerNode node={} />'.format(node))
            controllerNode  (self, node, self.G.nodes[node])
            controllerNode.q(self, node, self.G.nodes[node])
        # visit neighbors
        for v in self.G.successors(node):  # loop over all successors of this node
            # call controller for this node
            if controllerEdge is not None:
                if self.verbose: print(self.verbose_prefix, '<traverseRecursively_controllerEdge src={}, trg={} />'.format(node,v))
                controllerEdge  (self, node, self.G.nodes[node], v, self.G.nodes[v], self.G[node][v])
                controllerEdge.q(self, node, self.G.nodes[node], v, self.G.nodes[v], self.G[node][v])
            # recurse on neighbor
            self._traverseRecursively(v, controllerNode=controllerNode, controllerEdge=controllerEdge)
        return True

    def traverse(self, controllerGraph=None, controllerNode=None, controllerEdge=None, controllerMultiEdge=None):
        if self.verbose:
            prefix = self.verbose_prefix + '  '*self.level
            print(
                prefix,
                '<traverse level={}, controllerGraph={}, controllerNode={}, controllerEdge={}, controllerMultiEdge={}>'.format(
                    self.level,
                    controllerGraph is not None,
                    controllerNode is not None,
                    controllerEdge is not None,
                    controllerMultiEdge is not None
            ))
        assert controllerGraph     is None or controllerIsValid(controllerGraph    , AbstractControllerGraph    )
        assert controllerNode      is None or controllerIsValid(controllerNode     , AbstractControllerNode     )
        assert controllerEdge      is None or controllerIsValid(controllerEdge     , AbstractControllerEdge     )
        assert controllerMultiEdge is None or controllerIsValid(controllerMultiEdge, AbstractControllerMultiEdge)
        # call controller for graph
        if controllerGraph is not None:
            if self.verbose: print(prefix, '<traverse_controllerGraph>')
            controllerGraph(self, self.G.graph)
        # initialize first node of traversal (root)
        p = self.root   # set previous node
        u = self.root   # set current node
        V = list()      # get all successors of current node
        M = list()      # get all successors of diverging node
        # traverse graph (from the unique root to the unique end node)
        while u is not None:
            # gather info about current node
            predecessors  = list(self.G.predecessors(u))
            successors    = list(self.G.successors(u))
            nPredecessors = len(predecessors)
            # if 1 < nPredecessors, do not append its successors
            # until the current node visited sufficient times
            if 1 < nPredecessors and 0 < len(V):
                successors.clear()
            V.extend(successors)
            # assure topological ordering
            V = sorted(V)
            # check if current node has been visited by all of its predecessors
            if 1 < nPredecessors:
                if not '_traverse_n_visited' in self.G.nodes[u]:  # if is visited for the first time
                    self.G.nodes[u]['_traverse_n_visited'] = 1
                    nVisited = self.G.nodes[u]['_traverse_n_visited']
                else:  # otherwise node has been visited once or more
                    self.G.nodes[u]['_traverse_n_visited'] += 1
                    nVisited = self.G.nodes[u]['_traverse_n_visited']
                    if nVisited == nPredecessors:  # if visited by all its predecessors
                        self.G.nodes[u].pop('_traverse_n_visited')
            else:
                nVisited = nPredecessors
            # process current node
            if self.verbose:
                print(prefix, '  <traverse node={}, nPredecessors={}, nVisited={}, successors={}, V={}, M={} />'.format(
                        u, nPredecessors, nVisited, successors, V, M))
            if nVisited == nPredecessors:
                # finalize call to multi-edges controller (note: reverse order, finalize-then-call)
                if (1 < nPredecessors or (0 < len(M) and 0 == len(M[-1]))) and controllerMultiEdge is not None:  # if node has multiple edges (pointing in)
                    M.pop()
                    controllerMultiEdge.q(self, u, self.G.nodes[u], predecessors)
                    if self.verbose:
                        prefix = self.verbose_prefix + '  '*self.level
                        print(prefix, '  </traverse_controllerMultiEdge node={}, predecessors={}>'.format(u,predecessors))
                # call controller for current node
                if controllerNode is not None:
                    if self.verbose: print(prefix, '  <traverse_controllerNode node={} />'.format(u))
                    controllerNode  (self, u, self.G.nodes[u])
                    controllerNode.q(self, u, self.G.nodes[u])
                    try:
                        M[-1].remove(u)
                    except (ValueError, IndexError):
                        pass
                # call multi-edges controller (note: reverse order, finalize-then-call)
                if 1 < len(successors) and controllerMultiEdge is not None:  # if node has multiple edges (pointing out)
                    M.append(successors)
                    if self.verbose:
                        print(prefix, '  <traverse_controllerMultiEdge node={}, successors={} />'.format(u,successors))
                        prefix = prefix + '  '
                    controllerMultiEdge(self, u, self.G.nodes[u], successors)
                # call controller for edge connecting current node and next successor
                for v in successors:  # loop over all successors of this node
                    if controllerEdge is not None:
                        if self.verbose: print(prefix, '  <traverse_controllerEdge src={}, trg={} />'.format(u,v))
                        controllerEdge  (self, u, self.G.nodes[u], v, self.G.nodes[v], self.G[u][v])
                        controllerEdge.q(self, u, self.G.nodes[u], v, self.G.nodes[v], self.G[u][v])
            # set next node and update successors
            p = u
            try:
                u = V.pop(0)
            except IndexError:
                u = None
            except:
                raise
        # sanity check
        for u, data in self.G.nodes(data=True):
            assert '_traverse_n_visited' not in data.keys(), (
                f'node {u} is not visited by all of its predecessors'
            )
        # finalize controller for graph
        if controllerGraph is not None:
            controllerGraph.q(self, self.G.graph)
            if self.verbose: print(prefix, '</traverse_controllerGraph>')
        if self.verbose: print(prefix, '</traverse>')
        return True

    def traverseHierarchy(self, controllerGraph=None, controllerNode=None, controllerEdge=None, controllerMultiEdge=None):
        if self.verbose:
            print(self.verbose_prefix, '<traverseHierarchy controllerGraph={}, controllerNode={}, controllerEdge={}, controllerMultiEdge={}>'.format(
                    controllerGraph is not None, controllerNode is not None, controllerEdge is not None, controllerMultiEdge is not None
            ))
        # traverse nodes of graph
        ret = self.traverse(
                controllerGraph=controllerGraph,
                controllerNode=ControllerNode_TraverseHierarchy(controllerGraph, controllerNode, controllerEdge, controllerMultiEdge,
                                                                self.verbose, self.verbose_prefix),
                controllerEdge=controllerEdge,
                controllerMultiEdge=controllerMultiEdge)
        if self.verbose: print(self.verbose_prefix, '</traverseHierarchy>')
        return ret

    #-------------------
    # Hierarchical Graph
    #-------------------

    def _getClusterEdges(self, G, controllerMarkEdge):
        if self.verbose: print(self.verbose_prefix, '<_getClusterEdges>')
        assert controllerIsValid(controllerMarkEdge, AbstractControllerEdge)
        # separate edges based on the edge attribute
        clusterEdges = list()  # storage for edges of clusters
        for u, adjdict in G.adjacency():  # loop over all nodes
            # check if any edges are marked
            hasMarkedEdge = False
            for v, eattr in adjdict.items():  # loop over all neighbors
                tmpGraph = self._shallowCopy()
                tmpGraph._setGraph(G)
                ctrret   = controllerMarkEdge(tmpGraph, u, G.nodes[u], v, G.nodes[v], eattr)
                if ctrret == CtrRet.SUCCESS:
                    hasMarkedEdge = True
                    break
            # include only non-marked edges
            if not hasMarkedEdge:
                for v, eattr in adjdict.items():
                    clusterEdges.append((u, v))
        if self.verbose: print(self.verbose_prefix, '  </_getClusterEdges_result edges={}>'.format(clusterEdges))
        if self.verbose: print(self.verbose_prefix, '</_getClusterEdges>')
        return clusterEdges

    def _getClusterNodes(self, G, clusterEdges):
        if self.verbose: print(self.verbose_prefix, '<_getClusterNodes>')
        assert isinstance(clusterEdges, list) or \
               isinstance(clusterEdges, set), type(clusterEdges)
        # extract nodes of connected components
        subGraph  = G.edge_subgraph(clusterEdges)
        connNodes = networkx.weakly_connected_components(subGraph)
        # gather subgraph nodes in a list, and remove them from all nodes
        clusterNodes = list()
        allNodes     = set(G.nodes)
        for nodes in connNodes:  # loop over sets of nodes
            assert isinstance(nodes, set), type(nodes)
            clusterNodes.append(nodes)
            allNodes = allNodes.difference(nodes)
        # add remaining nodes
        for u in allNodes:
            if u == self.root:
                clusterNodes.insert(0, set([u]))
            else:
                clusterNodes.append(set([u]))
        if self.verbose: print(self.verbose_prefix, '  </_getClusterNodes_result nodes={}>'.format(clusterNodes))
        if self.verbose: print(self.verbose_prefix, '</_getClusterNodes>')
        return clusterNodes

    def _createTwoLevelGraph(self, G, clusterNodes, clusterType, controllerInitSubgraph=None):
        if self.verbose:
            print(
                self.verbose_prefix,
                '<_createTwoLevelGraph level={}, n_clusters={}, n_nodes_graph={}>'.format(
                    self.level, len(clusterNodes), G.number_of_nodes()))
        assert isinstance(clusterNodes, list), type(clusterNodes)
        assert isinstance(clusterType, str), type(clusterType)
        assert len(clusterNodes) <= G.number_of_nodes()
        assert controllerInitSubgraph is None or controllerIsValid(controllerInitSubgraph, AbstractControllerGraph)
        # exit if nothing to do (i.e., not more than one cluster)
        if len(clusterNodes) < 1 or G.number_of_nodes() <= len(clusterNodes):
            if self.verbose: print(self.verbose_prefix, '</_createTwoLevelGraph>')
            return None
        # create condensation
        H = networkx.condensation(G, clusterNodes)
        # setup condensed nodes
        for u in H.nodes():  # loop over all condensed nodes
            # get condensed nodes
            members = H.nodes[u]['members']
            if 1 < len(members):
                # create subgraph (with its own copy of attributes)
                S = G.subgraph(members).copy()
                S.graph['superNode']   = u
                S.graph['clusterType'] = clusterType
                assert self._isValid_nxGraph(S)
                sGraph = self._shallowCopy()
                sGraph.level += 1   # increase level (inherited from shallow copy)
                sGraph._setGraph(S) # setup graph
                if self.verbose: print(self.verbose_prefix, '  <_createTwoLevelGraph_createSubgraph subgraph_level={}/>'.format(sGraph.level))
                if controllerInitSubgraph is not None:
                    if self.verbose: print(self.verbose_prefix, '  <_createTwoLevelGraph_controllerInitSubgraph>')
                    controllerInitSubgraph  (sGraph, sGraph.G.graph)
                    controllerInitSubgraph.q(sGraph, sGraph.G.graph)
                    if self.verbose: print(self.verbose_prefix, '  </_createTwoLevelGraph_controllerInitSubgraph>')
                # update attributes of the condensed node
                H.nodes[u].update(S.graph)  # copy attributes of subgraph
                H.nodes[u]['obj'] = sGraph  # set subgraph as object
            else:
                v = list(members)[0]
                H.nodes[u].update(G.nodes[v])  # copy attributes of original node
        if self.verbose: print(self.verbose_prefix, '</_createTwoLevelGraph>')
        return H

    def extractHierarchicalGraph(self, controllerMarkEdge=None, controllerInitSubgraph=None):
        if self.verbose: print(self.verbose_prefix, '<extractHierarchicalGraph>')
        G = self.G
        # extract clusters by detecting nodes that indicate cluster begin/end
        #TODO why is this needed? how to improve?
        ctrDetectClusters = ControllerEdge_DetectClusters(self.verbose, self.verbose_prefix)
        self.traverse(controllerEdge=ctrDetectClusters)
        if ctrDetectClusters.clusterEdges is not None:
            clusterNodes = self._getClusterNodes(G, ctrDetectClusters.clusterEdges)
            H1 = self._createTwoLevelGraph(G, clusterNodes, 'clusterBeginEnd', controllerInitSubgraph=controllerInitSubgraph)
            if H1 is not None:
                H1.graph.update(G.graph)  # keep attributes of previous graph
                G = H1
        # extract clusters by using edge marker from the given `controllerMarkEdge`
        if controllerMarkEdge is not None:
            clusterEdges = self._getClusterEdges(G, controllerMarkEdge)
            clusterNodes = self._getClusterNodes(G, clusterEdges)
            H2 = self._createTwoLevelGraph(G, clusterNodes, 'clusterMarkEdge', controllerInitSubgraph=controllerInitSubgraph)
            if H2 is not None:
                H2.graph.update(G.graph)  # keep attributes of previous graph
                G = H2
        # init hierarchical graph as a shallow copy of `self`
        hGraph = self._shallowCopy()
        hGraph._setGraph(G, G.number_of_nodes() + 1)
        # create two-level graph at each node
        if controllerMarkEdge is not None:
            ctrCreateSubSubgraph = ControllerNode_CreateSubSubgraph(controllerMarkEdge, controllerInitSubgraph,
                                                                    self.verbose, self.verbose_prefix)
            hGraph.visit(controllerNode=ctrCreateSubSubgraph)
        if self.verbose: print(self.verbose_prefix, '</extractHierarchicalGraph>')
        return hGraph

    def isSubgraph(self):
        return 0 < self.level

    def nodeHasSubgraph(self, node):
        nodeAttribute = self.G.nodes[node]
        if 'obj' in nodeAttribute:
            return issubclass(type(nodeAttribute['obj']), BaseGraphNetworkX)
        else:
            return False

    def nodeGetSubgraph(self, node):
        assert self.nodeHasSubgraph(node)
        assert 'obj' in self.G.nodes[node]
        return self.G.nodes[node]['obj']

    def nodeSetSubgraph(self, node, sGraph):
        assert issubclass(type(sGraph), BaseGraphNetworkX), type(sGraph)
        self.G.nodes[node]['obj'] = sGraph

    #-----------
    # Plot Graph
    #-----------

    @staticmethod
    def linear_layout(nxGraph, node, posx=None, posy=None, pos_nodes=None):
        # initialize if non-recursive call
        if posx is None:        posx = 0.0
        if posy is None:        posy = 0.0
        if pos_nodes is None:   pos_nodes=dict()
        # set position for this node
        pos_nodes[node] = numpy.array([posx, posy])
        # recurse into neighboring nodes
        count = 0
        for nbr in list(nxGraph.successors(node)):  # loop over all neighbors
            BaseGraphNetworkX.linear_layout(nxGraph, nbr, posx+1.0, posy+float(count), pos_nodes)
            count += 1
        # reset y-position if leaf node (i.e., no successors)
        if not count:
            pos_nodes[node][1] = 0.0
        # return node positions
        return pos_nodes

    def plot(self, nodeLabels=False, edgeLabels=False):
        import copy
       #pos_nodes     = networkx.drawing.layout.circular_layout(self.G)
       #pos_nodes     = networkx.drawing.layout.kamada_kawai_layout(self.G)
       #pos_nodes     = networkx.drawing.layout.planar_layout(self.G)
       #pos_nodes     = networkx.drawing.layout.spring_layout(self.G)
       #pos_nodes     = networkx.drawing.layout.spectral_layout(self.G)
       #pos_nodes     = networkx.drawing.layout.spiral_layout(self.G)
        pos_nodes     = self.linear_layout(self.G, self.root)
        pos_sublabels = copy.deepcopy(pos_nodes)
        pos_suplabels = copy.deepcopy(pos_nodes)
        for node in pos_sublabels.keys():
            pos_sublabels[node][0] += 1.0e-1  #TODO not sure why this is the right amount of shifting
            pos_sublabels[node][1] += 5.0e-2  #TODO not sure why this is the right amount of shifting
        for node in pos_suplabels.keys():
            pos_suplabels[node][0] -= 1.0e-1  #TODO not sure why this is the right amount of shifting
            pos_suplabels[node][1] += 5.0e-2  #TODO not sure why this is the right amount of shifting
#       magn = 0.0
#       for pos in pos_sublabels.values():
#           magn = max(magn, abs(pos[1]))
#       for key in pos_sublabels.keys():
#           pos_sublabels[key][1] -= 0.2*magn
#       plot_options = {
#           'with_labels': True,
#           'node_size': 600,
#           'font_size': 8,
#       #   'font_weight': 'bold',
#       #   'labels': networkx.get_node_attributes(self.G, 'device'),
#       }
#       networkx.draw(self.G, pos_nodes, **plot_options)
#      #networkx.draw_networkx_edge_labels(self.G, pos_nodes)
        networkx.draw_networkx_nodes(self.G, pos_nodes, node_size=600)
        networkx.draw_networkx_edges(self.G, pos_nodes,
                                     min_source_margin=15,
                                     min_target_margin=15)
        networkx.draw_networkx_labels(self.G, pos_nodes, font_size=10)
        if nodeLabels:
            labels_device = networkx.get_node_attributes(self.G, 'device')
            labels_action = copy.deepcopy(labels_device)
            for node in labels_action.keys():
                if hasattr(self.G.nodes[node]['obj'], 'name'):
                    labels_action[node] = self.G.nodes[node]['obj'].name
                else:
                    labels_action[node] = ''
            networkx.draw_networkx_labels(self.G, pos_sublabels, labels=labels_device, font_size=6)
            networkx.draw_networkx_labels(self.G, pos_suplabels, labels=labels_action, font_size=6)
        if edgeLabels:
            networkx.draw_networkx_edge_labels(self.G, pos_nodes, font_size=6)

    #-------
    # UNUSED
    #-------

#TODO unused
    def nodeAttributeChange(self, nodeSource : int, nodeTarget : int, nodeAttributeName : str, defaultValue=None):
        assert isinstance(nodeSource, int), type(nodeSource)
        assert isinstance(nodeTarget, int), type(nodeTarget)
        assert isinstance(nodeAttributeName, str), type(nodeAttributeName)
        if nodeAttributeName in self.G.nodes[nodeSource]:
            valSrc = self.G.nodes[nodeSource][nodeAttributeName]
        else:
            valSrc = defaultValue
        if nodeAttributeName in self.G.nodes[nodeTarget]:
            valTrg = self.G.nodes[nodeTarget][nodeAttributeName]
        else:
            valTrg = defaultValue
        return (bool(valSrc is None) != bool(valTrg is None)) or (valSrc != valTrg)

#TODO unused
    def markEdgesWithAttributeChange(self, nodeAttributeName : str, edgeAttributeName : str):
        assert isinstance(nodeAttributeName, str), type(nodeAttributeName)
        assert isinstance(edgeAttributeName, str), type(edgeAttributeName)
        for u, v in self.G.edges:
            self.G[u][v][edgeAttributeName] = self.nodeAttributeChange(u, v, nodeAttributeName)
        return edgeAttributeName

#TODO unused
    def _createSubgraph_NetworkX(self, subBounds : tuple):
        assert isinstance(subNodeBounds, tuple), type(subNodeBounds)
        assert len(subNodeBounds) == 2, len(subNodeBounds)
        assert isinstance(subNodeBounds[0], int), type(subNodeBounds[0])
        assert isinstance(subNodeBounds[1], int), type(subNodeBounds[1])
        simplePaths = networkx.all_simple_paths(self.G, subBounds[0], subBounds[1])
        subNodes    = set(*simplePaths)
        return self.G.subgraph(list(subNodes))

    #-------------
    # Pruned Graph OLD
    #-------------

    def _toPrunedGraph_NetworkX(self, edgeAttributeName : str):
        ''' see also: https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.subgraph.html '''
        assert isinstance(edgeAttributeName, str), type(edgeAttributeName)
        cpGraph = networkx.DiGraph()  # copy of nodes/edges from full graph
        rmNodes = set()               # storage for removed nodes
        cpGraph.add_node(self.root, **self.G.nodes[self.root])
        # separate graph in nodes/edges to keep and to remove
        for u, nbrsdict in self.G.adjacency():
            keep = False
            for v, eattr in nbrsdict.items():
                assert edgeAttributeName in eattr
                if eattr[edgeAttributeName]:
                    keep = True
                    break
            if keep:
                # copy target nodes and edges
                for v, eattr in nbrsdict.items():
                    cpGraph.add_node(v, **self.G.nodes[v])
                    if u in cpGraph:
                        cpGraph.add_edge(u, v, **eattr)
            else:
                # store source node of removed edge
                rmNodes.add(u)
        # connect "loose" nodes in pruned graph
        for u in rmNodes:
            if not u in cpGraph:
                continue
            targets = []
            candidates = list(self.G.successors(u))
            while candidates:  # while candidates remain
                v = candidates.pop()
                if v in cpGraph:
                    targets.append(v)
                else:
                    candidates.extend(list(self.G.successors(v)))
            for v in targets:
                cpGraph.add_edge(u, v)
        return cpGraph

    def toPrunedGraph(self, edgeAttributeName : str):
        if self.verbose:
            print(self.verbose_prefix, 'Create pruned graph based on edge attribute:', edgeAttributeName)
        graph = self._shallowCopy()
        graph._setGraph(self._toPrunedGraph_NetworkX(edgeAttributeName), self._nodeid)
        return graph

    #-------------------
    # Hierarchical Graph OLD
    #-------------------

    def _toHierarchicalGraph_separateEdges(self, edgeAttributeName : str):
        assert isinstance(edgeAttributeName, str), type(edgeAttributeName)
        # separate edges based on the edge attribute
        coarseEdges = list()  # storage for edges of coarse graph
        subEdges    = list()  # storage for edges of (fine) subgraphs
        for u, adjdict in self.G.adjacency():
            isCoarseEdge = False
            adjitems = adjdict.items()
            for v, eattr in adjitems:
                if edgeAttributeName in eattr and eattr[edgeAttributeName]:
                    isCoarseEdge = True
                    break
            if isCoarseEdge:
                for v, eattr in adjitems:
                    coarseEdges.append((u, v))
            else:
                for v, eattr in adjitems:
                    subEdges.append((u, v))
        return coarseEdges, subEdges

    def _toHierarchicalGraph_createSubGraphs(self, subEdges : list):
        assert isinstance(subEdges, list), type(subEdges)
        # extract nodes of connected components
        edgeGraph = self.G.edge_subgraph(subEdges)
        connNodes = networkx.weakly_connected_components(edgeGraph)
        allNodes  = set(self.G.nodes)
        # create subgraphs
        subGraphs = list()
        for nodes in connNodes:  # loop over sets of nodes
            allNodes = allNodes.difference(nodes)
            subGraphs.append(self.G.subgraph(nodes).copy())
            assert self._isValid_nxGraph(subGraphs[-1])
        for node in allNodes:  # loop over individual nodes
            subGraphs.append(self.G.subgraph(node).copy())
        return subGraphs

    def _toHierarchicalGraph_createHierarchicalGraph(self, subGraphs : list, coarseEdges : list):
        assert isinstance(subGraphs, list), type(subGraphs)
        assert isinstance(coarseEdges, list), type(coarseEdges)
        # init hierarchical graph as a shallow copy of `self`
        hGraph = self._shallowCopy()
        # add subgraphs as nodes in hierarchical graph; get bounds of all subgraphs
        boundsSG = dict()
        for SG in subGraphs:
            node = hGraph.addNode(SG)
            boundsSG[node] = self._searchBounds(SG)
            for attributeName, attributeValue in self.G.nodes[boundsSG[node][0]].items():
                if attributeName in hGraph.G.nodes[node]:
                    continue
                hGraph.setNodeAttribute(node, attributeName, attributeValue)
        # translate edges for hierarchical graph
        hEdges = list()
        for edge in coarseEdges:  # loop over all coarse edges
            nodeSource = nodeTarget = hGraph.root - 1
            for i, b in boundsSG.items():  # loop over all subgraph bounds
                if nodeSource < hGraph.root and edge[0] == b[1]:
                    nodeSource = i
                if nodeTarget < hGraph.root and edge[1] == b[0]:
                    nodeTarget = i
            assert hGraph.root <= nodeSource and hGraph.root <= nodeTarget
            hEdges.append((nodeSource, nodeTarget))
        # link subgraphs / coarse nodes
        for j, edge in enumerate(hEdges):
            hGraph.addEdge(*edge)
            for attributeName, attributeValue in self.G.edges[coarseEdges[j]].items():
                hGraph.G.edges[edge][attributeName] = attributeValue
        return hGraph

    def toHierarchicalGraph(self, edgeAttributeName : str):
        if self.verbose:
            print(self.verbose_prefix, 'Create hierarchical graph based on edge attribute:', edgeAttributeName)
        coarseEdges, subEdges = self._toHierarchicalGraph_separateEdges(edgeAttributeName)
        subGraphs             = self._toHierarchicalGraph_createSubGraphs(subEdges)
        return                  self._toHierarchicalGraph_createHierarchicalGraph(subGraphs, coarseEdges)

