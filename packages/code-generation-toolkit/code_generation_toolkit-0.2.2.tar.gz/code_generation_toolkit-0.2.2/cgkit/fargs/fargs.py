import transpyle.general
import transpyle.fortran
import transpyle.python
import horast.nodes
import typed_ast.ast3
import copy
import json

class Fargs(typed_ast.ast3.NodeVisitor):
    def __init__(self, enable_debug=False, **kwargs):
        assert isinstance(enable_debug, bool), type(enable_debug)
        self.tree         = None
        self.functions    = None
        self.enable_debug = enable_debug
        if self.enable_debug:  print('[Fname] All variables:', str(self.__dict__))

    def convert_fortran_to_tree(self, path):
        '''Create Fortan-AST from Fortran code.

        Transpyle tools used:
        Reader --- Reads the code
        Parser --- Creates a Fortran-AST
        '''
        reader = transpyle.general.CodeReader()
        parser = transpyle.fortran.FortranParser()
        # process code
        input_code = reader.read_file(path)
        return parser.parse(input_code, path)

    def generalize_tree(self, tree):
        '''Transforms Fortran-AST into a general purpose AST that can be easily
        processed and unparsed into many outputs.

        Transpyle tools used:
        Generalizer --- Transforms Fortran-AST into a general purpose AST
        '''
        generalizer = transpyle.fortran.FortranAstGeneralizer()
        # process tree
        return generalizer.generalize(tree)

    def dump_tree(self, node, annotate_fields=True, include_attributes=False, indent='  '):
        """
        Return a formatted dump of the tree in *node*.  This is mainly useful for
        debugging purposes.  The returned string will show the names and the values
        for fields.  This makes the code impossible to evaluate, so if evaluation is
        wanted *annotate_fields* must be set to False.  Attributes such as line
        numbers and column offsets are not dumped by default.  If this is wanted,
        *include_attributes* can be set to True.
        """
        def _format(node, level=0):
            if isinstance(node, typed_ast.ast3.AST):
                fields = [(a, _format(b, level)) for a, b in typed_ast.ast3.iter_fields(node)]
                if include_attributes and node._attributes:
                    fields.extend([(a, _format(getattr(node, a), level))
                                   for a in node._attributes])
                return ''.join([
                    node.__class__.__name__,
                    '(',
                    ', '.join( ('%s=%s' % field for field in fields) if annotate_fields else
                               (b for a, b in fields) ),
                    ')'])
            elif isinstance(node, list):
                lines = ['[']
                lines.extend((indent * (level + 2) + _format(x, level + 2) + ','
                             for x in node))
                if len(lines) > 1:
                    lines.append(indent * (level + 1) + ']')
                else:
                    lines[-1] += ']'
                return '\n'.join(lines)
            return repr(node)

        if not isinstance(node, (typed_ast.ast3.AST, list)):
            raise TypeError('expected AST or list, got %r' % node.__class__.__name__)
        return _format(node)

    def write_tree(self, tree, path) -> None:
        with open(path, 'w') as f:
            f.write(self.dump_tree(tree, annotate_fields=False, include_attributes=False))
            f.close()

    def write_functions(self, path):
        functions_output = copy.deepcopy(self.functions)
        # convert node objects to strings
        for data in functions_output.values():
            data['node'] = str(data['node'])
            for declaration in data['declarations'].values():
                for var in declaration.values():
                    var['node'] = str(var['node'])
        # write JSON file
        with open(path, 'w') as f:
            json.dump(functions_output, f, indent=4)

    def visit_FunctionDef(self, node):
        self.functions[node.name] = {'node': node}
        self.generic_visit(node)

    def visit_StaticallyTypedFunctionDefClass(self, node):
        self.visit_FunctionDef(node)

    def getFunctions(self, arg):
        # convert file to tree
        if isinstance(arg, typed_ast.ast3.AST):
            self.tree = arg
        else:
            self.tree = self.convert_fortran_to_tree(arg)
            self.tree = self.generalize_tree(self.tree)
        # check tree
        assert self.tree is not None
        assert isinstance(self.tree, typed_ast.ast3.AST), type(self.tree)
        # get functions from tree
        self.functions = dict()
        self.visit(self.tree)
        if self.enable_debug:  print('[Fname.getFunctions] names:', [name for name in self.functions.keys()])
        return self.functions

    def getArgs(self):
        assert self.functions is not None
        assert isinstance(self.functions, dict), type(self.functions)
        for name, data in self.functions.items():
            data['args'] = [a.arg for a in data['node'].args.args]
            if self.enable_debug:  print('[Fname.getArgs] args of {}:'.format(name), data['args'])
        return self.functions

    def _isDeclaration(self, node, node_next):
        if isinstance(node, typed_ast.ast3.AnnAssign) and \
           isinstance(node_next, horast.nodes.Comment) and \
           'Fortran metadata' in node_next.comment:
            meta_str = node_next.comment[node_next.comment.find('{'):]
            metadata = typed_ast.ast3.literal_eval(meta_str)
            if 'is_declaration' in metadata:
                is_decl = metadata['is_declaration']
                del metadata['is_declaration']
            else:
                is_decl = False
            return is_decl, metadata
        else:
            return False, None

    def getDeclarations(self):
        assert self.functions is not None
        assert isinstance(self.functions, dict), type(self.functions)
        # get declarations
        for data in self.functions.values():
            data['declarations'] = {'in':dict(), 'out':dict(), 'inout':dict(), 'local':dict()}
            for i in range(len(data['node'].body) - 1): # loop over all node pairs
                isDeclaration, metadata = self._isDeclaration(data['node'].body[i  ],
                                                              data['node'].body[i+1])
                if not isDeclaration:
                    continue
                # get node
                node = data['node'].body[i]
                # get name
                assert isinstance(node.target, typed_ast.ast3.Name), type(node.target)
                name = node.target.id
                # set intent if not defined
                if not 'intent' in metadata:
                    if name in data['args']:
                        metadata['intent'] = 'inout'
                    else:
                        metadata['intent'] = 'local'
                # get type
                if isinstance(node.annotation, typed_ast.ast3.Name) and node.annotation.id in ['bool', 'float', 'int', 'str']:
                    vtype = node.annotation.id
                else:
                    vtype = 'array'
                # add entry to variables dict
                assert metadata['intent'] in data['declarations'].keys(), metadata['intent']
                vdict = data['declarations'][metadata['intent']]
                vdict[name] = {'type': vtype}
                vdict[name].update(metadata)
                vdict[name]['node'] = node
            # check output
            if self.enable_debug:
                print('[Fname.getDeclarations] #args: total', len(data['node'].args.args))
                print('[Fname.getDeclarations] #decl:',
                      'in',    len(data['declarations']['in']),
                      'out',   len(data['declarations']['out']),
                      'inout', len(data['declarations']['inout']),
                      'local', len(data['declarations']['local']))
            assert len(data['node'].args.args) == (len(data['declarations']['in']) + \
                                                   len(data['declarations']['out']) + \
                                                   len(data['declarations']['inout']))
        return self.functions

