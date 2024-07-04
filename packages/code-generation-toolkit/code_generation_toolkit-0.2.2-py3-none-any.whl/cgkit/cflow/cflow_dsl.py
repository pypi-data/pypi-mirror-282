import cgkit.cflow.utils_cflow_dsl as utils
import cgkit.cflow.node as node

def initializeCodeGenerator(codeAssembler):
    return utils.initialize(codeAssembler)

def finalizeCodeGenerator(basename=None):
    # perform setup and parse code
    utils.setUp()
    parsedCode = utils.parseCode()
    if parsedCode is not None:
        driverCode, subroutineCode = parsedCode
        if basename is not None:
            # write driver code
            if driverCode is not None:
                with open('_code_{}_driver.cpp'.format(basename), 'w') as f:
                    f.write(driverCode)
            # write subroutine code
            if subroutineCode is not None:
                for nameSub, codeSub in subroutineCode.items():
                    with open('_code_{}_{}.cpp'.format(basename, nameSub), 'w') as f:
                        f.write(codeSub)
    return utils.finalize()

def Iterator(iterType : str):
    obj = node.IteratorNode(iterType)
    return utils.addNodeAndLink(None, obj)

def ConcurrentDataBegin(Uin=[], scratch=[]):
    obj = node.ConcurrentDataBeginNode(Uin, scratch)
    def linkfn(sourceNode):  # depends on `obj`
        assert sourceNode is not None
        return utils.addNodeAndLink(sourceNode, obj)
    return linkfn

def ConcurrentDataEnd(Uout, **kwargs):
    obj = node.ConcurrentDataEndNode(Uout)
    def linkfn(sourceNode):  # depends on `obj`
        assert sourceNode is not None
        return utils.addNodeAndLink(sourceNode, obj)
    return linkfn

def Action(name : str, args=list()):
    obj = node.ActionNode(name, args)
    def linkfn(sourceNode):  # depends on `obj`
        assert sourceNode is not None
        return utils.addNodeAndLink(sourceNode, obj)
    return linkfn

def ConcurrentHardware(**kwargs):
    for device, info in kwargs.items():
        nodes = info['actions']
        utils.setDevice(nodes, device)
        for key, value in info.items():
            if 'actions' == key:
                continue
            utils.setAttribute(nodes, key, value)
    return
