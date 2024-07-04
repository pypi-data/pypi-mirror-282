'''
TODO
- create variables to replace _connector, _link, _param
  such that users can choose their own prefix & postfix strings (`lstr` and `rstr`)
- use packages for parameter/string substitution
- when linking trees check if added parameters are declared

QUESTIONS
- can template code look simpler than parsed code?
- why not use #ifdef's?
  -> need examples that are too complex for #ifdef's
- why not use C++ templates?
  -> fine-grain control over code/optimizations at granularity of lines
- when can we justify to use these templates/boilerplates?
  what are complex enough examples that demonstrate the usage of this?
- how to find and track bugs?
'''

import copy, json, pathlib, re

KEY_CONNECTOR    = '_connector'
KEY_LINK         = '_link'
KEY_CODE         = '_code'
KEY_PARAM        = '_param'
KEY_PARAM_FILE   = KEY_PARAM+':__file__'
KEY_PARAM_TYPE   = KEY_PARAM+':__type__'
KEY_PARAM_INDENT = KEY_PARAM+':__indent__'

LINK_PATH_FROM_STACK = '__LINK_PATH_FROM_STACK__'

class SourceTree():
    def __init__(self, codePath=pathlib.Path('.'), indentSpace=' '*4,
                 template_type='regex', verbose=True, verbosePre=r'/* ',
                 verbosePost=r' */', debug=False, debugPrefix='[SourceTree]'):
        if isinstance(codePath, pathlib.Path):
            self.codePath = codePath
        else:
            self.codePath = pathlib.Path(codePath)
        self.indentSpace     = indentSpace
        self.template_type   = template_type
        self.verbose         = verbose
        self.verbosePre      = verbosePre
        self.verbosePost     = verbosePost
        self.debug           = debug
        self.debugPrefix     = debugPrefix
        self.tree            = None
        self._linkPathLookup = None  # dictionary of all link paths
        self._linkStack      = None  # stack with history of used links
        self._pathStack      = None  # stack with history of used paths corresponding to `_linkStack`

    def initTree(self, filename, parameters=None):
        ''' Initializes the source tree. '''
        self.tree            = load(self.codePath / filename)
        self._linkPathLookup = linkPaths_search(self.tree)
        self._linkStack      = list()
        self._pathStack      = dict()
        if parameters is not None:
            assert isinstance(parameters, dict), type(parameters)
            for key, value in parameters.items():
                assert key.startswith(KEY_PARAM)
                self.tree[key] = value
        return

    @staticmethod
    def _navigate_path(tree, path=None):
        ''' Goes through each link path and checks the type. '''
        assert isinstance(tree, dict), type(tree)
        if path is None:
            pass
        else:
            assert linkPath_checkType(path), type(path)
            for p in path:
                tree = tree[p]
        return tree

    def getTree(self, path=None):
        ''' Navigates along the given path and returns a tree that is rooted
            where the path ends. '''
        assert self.tree is not None, 'Tree does not exist, call initTree() first'
        return self._navigate_path(self.tree, path)

    def getLinkPathKeys(self):
        """ Returns a list of the keys for each link in the tree from the tree path dictionary. -A """
        assert self._linkPathLookup is not None
        return list(self._linkPathLookup.keys())

    def getLastLinkPath(self, linkKey=None):
        """ Returns the last link path in the tree path dictionary. -A """
        assert self._linkPathLookup is not None
        if isinstance(linkKey, str):
            if linkKey in self._linkPathLookup:
                return self._linkPathLookup[linkKey][-1]
            else:
                return None
        else:
            if linkKey is None:
                linkKey = self.getLinkPathKeys()
            linkPath = dict()
            for key in linkKey:
                if key in self._linkPathLookup:
                    linkPath[key] = self._linkPathLookup[key][-1]
                else:
                    linkPath[key] = None
            return linkPath

    def _pushPath(self, linkInfo, path=None):
        """ What is kl?
        Checks if there is a path stack from the used paths, if not then the tree is not initialized
        Tentative: Adds a new path to the path stack using the provided linkInfo
        -A
         """
        assert self._pathStack is not None, 'Path stack does not exist, call initTree() first'
        if self.debug: print(self.debugPrefix, 'Push path(s) to stack (before):', self._pathStack)
        if isinstance(linkInfo, dict):
            for kl, path in linkInfo.items():
                if kl in self._pathStack:
                    self._pathStack[kl].append(path)
                else:
                    self._pathStack[kl] = [path]
        elif isinstance(linkInfo, str):
            assert linkPath_checkType(path), type(path)
            kl = linkInfo
            if kl in self._pathStack:
                self._pathStack[kl].append(path)
            else:
                self._pathStack[kl] = [path]
        else:
            raise NotImplementedError('Unknown type {}'.format(type(linkInfo)))
        if self.debug: print(self.debugPrefix, 'Push path(s) to stack (after): ', self._pathStack)

    def _popPath(self, linkKey):
        """
        Unsure of what "kl" is signifying, assume keyLink but unsure of how it is used in each method
        Returns the path information to get to a specific linkKey
        -A
        """
        assert self._pathStack is not None, 'Path stack does not exist, call initTree() first'
        if self.debug: print(self.debugPrefix, 'Pop path(s) from stack (before):', self._pathStack)
        pathInfo = None
        try:
            pathInfo = {kl: self._pathStack[kl].pop() for kl in linkKey}
        except KeyError:
            assert isinstance(linkKey, str), type(linkKey)
            pathInfo = {linkKey: self._pathStack[linkKey].pop() }
        except:
            raise
        if self.debug: print(self.debugPrefix, 'Pop path(s) from stack (after): ', self._pathStack)
        return pathInfo

    def getLinkPath(self, linkKey=None):
        """
        linkKey = list or string or none specified
        Returns the path that goes to each link in the path stack
        -A
        """
        assert self._pathStack is not None, 'Path stack does not exist, call initTree() first'
        if isinstance(linkKey, list):
            return [self._pathStack[kl][-1] for kl in linkKey]
        elif isinstance(linkKey, str):
            return self._pathStack[linkKey][-1]
        elif linkKey is None:
            return [path[-1] for path in self._pathStack.values() if path]
        else:
            raise NotImplementedError('Unknown type {}'.format(type(linkKey)))

    def pushLink(self, linkKey):
        """
        Adds the link key to the top of the stack
        -A
        """
        if self.debug: print(self.debugPrefix, 'Push link(s) to stack (before):', self._linkStack)
        assert self._linkStack is not None, 'Link stack does not exist, call initTree() first'
        if isinstance(linkKey, list):
            pass
        elif isinstance(linkKey, str):
            linkKey = [linkKey]
        else:
            raise NotImplementedError('Unknown type {}'.format(type(linkKey)))
        self._linkStack.append(linkKey)
        if self.debug: print(self.debugPrefix, 'Push link(s) to stack (after): ', self._linkStack)
        self._pushPath(self.getLastLinkPath(linkKey))

    def popLink(self):
        """
        Pops the path information for the link on the top of the stack -A
        """
        assert self._linkStack is not None, 'Link stack does not exist, call initTree() first'
        if self.debug: print(self.debugPrefix, 'Pop link(s) from stack (before):', self._linkStack)
        linkKey = self._linkStack.pop()
        if self.debug: print(self.debugPrefix, 'Pop link(s) from stack (after): ', self._linkStack)
        pathInfo = self._popPath(linkKey)
        return pathInfo

#   def copy(self):
#       ''' TODO '''
#       return SourceTree(codePath=self.codePath, indentSpace=self.indentSpace,
#                         verbose=self.verbose, debug=self.debug)

    def dump(self, path, indentNSpaces=2):
        ''' TODO '''
        assert self.tree is not None, 'Tree does not exist, call initTree() first'
        return dump(self.tree, path, indentNSpaces)

    def link(self, tree2link, linkPath=None, parameters=None):
        ''' Attach each connector of `tree2link` to the corresponding links of
            this tree. '''
        # setup tree that will be linked
        if isinstance(tree2link, dict):
            pass
        elif isinstance(tree2link, str) or isinstance(tree2link, pathlib.Path):
            tree2link = load(tree2link)
        else:
            raise TypeError('Expected dict or filepath, but got {}'.format(type(tree2link)))
        # perform linking
        if linkPath == LINK_PATH_FROM_STACK:
            # link with paths from the (internal) stack
            pathInfo = dict()  # init return variable
            forest   = split_connectors(tree2link)
            for t2l in forest:
                connKey = search_connectors(t2l).pop()
                linkKey = convert_key_from_connector_to_link(connKey)
                path    = self.getLinkPath(linkKey)
                if self.debug: print(self.debugPrefix, 'Attach connector "{}" at path={}'.format(connKey, path))
                info    = self._linkAtPath(t2l, linkPath_shorten(path, shortenTo=KEY_CODE, including=True), parameters)
                assert set(pathInfo.keys()).isdisjoint(set(info.keys()))
                pathInfo.update(info)
            return pathInfo
        else:
            # link with a given path from arguments
            if linkPath is not None:
                if KEY_LINK in linkPath[-1]:
                    linkPath = linkPath_shorten(linkPath, shortenTo=KEY_CODE, including=True)
            else:
                linkPath = linkPath_new()
            if self.debug: print(self.debugPrefix, 'Attach tree at path={}'.format(linkPath))
            return self._linkAtPath(tree2link, linkPath, parameters)

    def _linkAtPath(self, tree2link, linkPath, parameters=None):
        """
        Connects the tree that results from the link path to the tree2link,
        updates the linkPaths dictionary and updates the path information.
        -A
        """
        assert linkPath_checkType(linkPath), type(linkPath)
        # navigate tree to the linking path, denote result as `tp`
        tp = self.getTree(linkPath)
        # perform linking of `tree2link` into `tp`
        pathInfo = self.linkTrees(tp, tree2link, parameters)
        if pathInfo is None or not pathInfo:
            raise RuntimeError('Error in linkTrees()')
        # augment paths with the full information; and update `_linkPathLookup`
        for connKey, pathList in pathInfo.items():
            for i, path in enumerate(pathList):
                pathInfo[connKey][i] = linkPath_extend(linkPath, path)                 # add prefix to path
                newLinkPaths         = linkPaths_search(self._navigate_path(tp, path)) # find new link paths
                self._linkPathLookup = linkPaths_extend(self._linkPathLookup, pathInfo[connKey][i], newLinkPaths)
        return pathInfo

    @staticmethod
    def linkTrees(tree, tree2link, parameters=None):
        ''' Attach each connector of `tree2link` to the corresponding link in
            the code of `tree`.  Returns `connInfo` that contains the paths to
            the linked tree. '''
        assert isinstance(tree, dict), type(tree)
        assert isinstance(tree2link, dict), type(tree2link)
        assert parameters is None or isinstance(parameters, dict), type(parameters)
        # exit if nothing to do
        if not (KEY_CODE in tree):  # if code does not exists in `tree`
            return None
        # setup parameters and get top-level parameters of to-be-linked tree
        if parameters is not None:
            parameters = copy.deepcopy(parameters)
        else:
            parameters = dict()
        _gather_parameters(tree2link, parameters)
        # find all potential link locations in code
        linkInfo = search_links_in_code(tree[KEY_CODE])
        # perform linking
        connInfo = dict()  # init return variable
        for connKey in search_connectors(tree2link):
            # convert connector key into link key
            linkKey = convert_key_from_connector_to_link(connKey)
            if not (linkKey in linkInfo.keys()):
                raise RuntimeError('The matching link {} for connector {} does not exist; '.format(linkKey, connKey) + \
                                   'available links: {}'.format(linkInfo.keys()))
            # setup tree that is to be linked: copy and inherit parameters
            tl = copy.deepcopy(tree2link[connKey])
            for key, value in parameters.items():
                assert key.startswith(KEY_PARAM)
                if not key in tl:
                    tl[key] = value
            # attach/append connector to link
            connInfo[connKey] = list()
            for i in linkInfo[linkKey]:
                tree[KEY_CODE][i][linkKey].append(tl)
                j = len(tree[KEY_CODE][i][linkKey]) - 1
                connInfo[connKey].append( linkPath_new(KEY_CODE, i, linkKey, j) )
        return connInfo

    def parse(self):
        ''' TODO '''
        assert self.tree is not None, 'Tree does not exist, call initTree() first'
        # write debug file
        if self.debug:
            try:
                cl = self.__class__.__name__
                fn = self.tree[KEY_PARAM_FILE]
                name = '{}_{}'.format(cl, fn)
            except KeyError:
                cl = self.__class__.__name__
                name = '{}'.format(cl)
            except:
                raise
            dump(self.tree, '_debug_{}.json'.format(name))
        # parse tree
        lines      = list()
        parameters = dict()
        self.parseTree(self.tree, lines, parameters, self.indentSpace, 0, self.template_type,
                       self.verbose, self.verbosePre, self.verbosePost)
        # parse lines
        return '\n'.join(lines)

    @staticmethod
    def parseTree(tree, lines, parameters, indentSpace, indentCount, template_type, verbose, verbosePre, verbosePost):
        ''' TODO '''
        assert isinstance(tree, dict), type(tree)
        assert isinstance(lines, list), type(lines)
        assert isinstance(parameters, dict), type(parameters)
        # gather parameters
        indentCount += _gather_parameters(tree, parameters)
        indentStr    = indentSpace * indentCount
        try:
            whichFile = parameters[KEY_PARAM_FILE]
            whichType = parameters[KEY_PARAM_TYPE]
        except KeyError:
            whichFile = None
            whichType = None
        # process tree
        hasConn = False
        hasCode = False
        hasLink = False
        for key in tree.keys():
            # set string for verbose output
            if whichFile:
                verboseTag = key+' file="{}"'.format(whichFile)
            else:
                verboseTag = key
            # parse depending on the current key
            if key.startswith(KEY_CONNECTOR):
                hasConn = True
                # skip over connector
                if verbose: lines.append(indentStr + SourceTree._verbose_begin(verboseTag, verbosePre, verbosePost))
                SourceTree.parseTree(tree[key], lines, copy.deepcopy(parameters), indentSpace, indentCount, template_type,
                                     verbose, verbosePre, verbosePost)
                if verbose: lines.append(indentStr + SourceTree._verbose_end(verboseTag, verbosePre, verbosePost))
            elif key == KEY_CODE:
                hasCode = True
                # process lines of code
                if verbose: lines.append(indentStr + SourceTree._verbose_begin(verboseTag, verbosePre, verbosePost))
                for c in tree[KEY_CODE]:
                    if isinstance(c, str):
                        lines.append(_parse_line(whichType, _substitute_parameters(c, parameters, template_type), indentSpace, indentCount))
                    elif isinstance(c, dict):
                        SourceTree.parseTree(c, lines, copy.deepcopy(parameters), indentSpace, indentCount, template_type,
                                             verbose, verbosePre, verbosePost)
                    else:
                        raise TypeError('Expected str or dict, but got {}'.format(type(c)))
                if verbose: lines.append(indentStr + SourceTree._verbose_end(verboseTag, verbosePre, verbosePost))
            elif key.startswith(KEY_LINK):
                hasLink = True
                # recurse into links
                if verbose: lines.append(indentStr + SourceTree._verbose_begin(verboseTag, verbosePre, verbosePost))
                for lt in tree[key]:
                    SourceTree.parseTree(lt, lines, copy.deepcopy(parameters), indentSpace, indentCount, template_type,
                                         verbose, verbosePre, verbosePost)
                if verbose: lines.append(indentStr + SourceTree._verbose_end(verboseTag, verbosePre, verbosePost))
            elif key.startswith(KEY_PARAM):
                continue
            else:
                raise SyntaxError('Unknown key: {}'.format(key))
        assert 1 == sum([hasConn, hasCode, hasLink]), (hasConn, hasCode, hasLink)

    @staticmethod
    def _verbose_begin(tag, verbosePre, verbosePost):
        return verbosePre + r'<' + tag + r'>' + verbosePost

    @staticmethod
    def _verbose_end(tag, verbosePre, verbosePost):
        return verbosePre + r'</' + tag + r'>' + verbosePost

#########################
# Link Path
#########################

def linkPath_checkType(path):
    return isinstance(path, tuple)

def linkPath_new(*args):
    assert linkPath_checkType(args), type(args)
    return args

def linkPath_extend(path, *args):
    """
    Extends the link path by the arguments given and returns the extended path in a tuple. -A
    """
    extPath = list(path)
    for p in args:
        extPath.extend(p)
    return tuple(extPath)

def linkPath_shorten(path, shortenTo=KEY_CODE, including=True):
    """
    Shortens the link path to all but the last element and returns
    the path in a tuple. -A
    """
    if isinstance(path, tuple):
        path = list(path)
    rePath = path.copy()
    rePath.reverse()
    for val in rePath:
        if val == shortenTo and not including:
            break
        if val == shortenTo and including:
            path = path[:-1]
            break
        else:
            path = path[:-1]
    return tuple(path)

#########################
# Link Path Dictionaries
#########################

def linkPaths_search(tree, linkPathLookup=None, pathPrefix=list()):
    ''' Searches all paths that navigate to a link. Search is performed
        recursively (arguments `linkPathLookup` and `pathPrefix` are used during
        recursion). '''
    assert isinstance(tree, dict), type(tree)
    assert linkPathLookup is None or isinstance(linkPathLookup, dict), type(linkPathLookup)
    assert isinstance(pathPrefix, list), type(pathPrefix)
    # initialize path dict
    if linkPathLookup is None:
        linkPathLookup = dict()
    # get all connectors
    connector = search_connectors(tree)
    if not connector:
        connector.append(None)
    # search paths to links
    for connKey in connector:
        # step past a connector
        if connKey is not None:
            assert KEY_CODE in tree[connKey]
            path =     [connKey, KEY_CODE]  # initialize path
            code = tree[connKey][KEY_CODE]  # get code lines
        else:
            assert KEY_CODE in tree
            path =     [KEY_CODE]  # initialize path
            code = tree[KEY_CODE]  # get code lines
        # visit all link locations in code
        linkInfo = search_links_in_code(code)
        for linkKey, linkLocation in linkInfo.items():
            for i in linkLocation:
                # add path to search results
                if linkKey in linkPathLookup:
                    linkPathLookup[linkKey].append( linkPath_extend(pathPrefix, path, [i, linkKey]) )
                else:
                    linkPathLookup[linkKey] = [ linkPath_extend(pathPrefix, path, [i, linkKey]) ]
                # recurse into sub-trees at current link
                for j, tl in enumerate(code[i][linkKey]):
                    linkPaths_search(tl, linkPathLookup, pathPrefix+path+[i, linkKey, j])
    # return the search results
    return linkPathLookup

def linkPaths_extend(linkPathLookup, pathPrefix, linkPathExtend):
    """
    Adds a link path to the dictionary of all link paths. -A
    """
    assert isinstance(linkPathLookup, dict), type(linkPathLookup)
    assert isinstance(linkPathExtend, dict), type(linkPathExtend)
    assert linkPath_checkType(pathPrefix), type(pathPrefix)
    for key, pathList in linkPathExtend.items():  # loop over all path types
        for pathExtend in pathList:               # loop over all paths of one type
            path = linkPath_extend(pathPrefix, pathExtend)
            if key in linkPathLookup:
                linkPathLookup[key].append(path)
            else:
                linkPathLookup[key] = [path]
    return linkPathLookup

#########################
# Utility Functions
#########################

def search_connectors(tree):
    ''' Gets all connectors at the top level of the tree. '''
    assert isinstance(tree, dict), type(tree)
    return [k for k in tree.keys() if k.startswith(KEY_CONNECTOR)]

def split_connectors(tree):
    ''' Splits connectors into subtrees. '''
    assert isinstance(tree, dict), type(tree)
    # get connectors and parameters at the top level
    connector = search_connectors(tree)
    parameters = dict()
    _gather_parameters(tree, parameters)
    # split tree, where one tree is created for each connector
    forest = list()
    for connKey in connector:
        forest.append({connKey: tree[connKey]})
        forest[-1].update(copy.deepcopy(parameters))
    return forest

def convert_key_from_connector_to_link(connKey):
    ''' Converts a connector key into the corresponding link key. '''
    assert isinstance(connKey, str), type(connKey)
    assert connKey, connKey
    s = re.split(r'[:]{1}', connKey)
    if   1 == len(s):
        linkKey = KEY_LINK
    elif 2 == len(s):
        linkKey = KEY_LINK+':'+s[1]
    else:
        linkKey = None
        raise NotImplementedError('Connector key "{}" is not supported'.format(connKey))
    return linkKey

def search_links_in_code(code):
    """
    Searches for link embedded within the code and return the link information in a dictionary.  -A
    """
    assert isinstance(code, list), type(code)
    linkInfo = dict()
    for i, line in enumerate(code):  # loop over all code lines
        if isinstance(line, dict):
            # find unique link key
            linkKey = [k for k in line.keys() if k.startswith(KEY_LINK)]  # find all links
            if 1 == len(linkKey):
                linkKey = linkKey[0]
            else:
                raise RuntimeError('The number of links should be one, but is {}'.format(len(linkKey)))
            # add line in code, where the link was found
            if linkKey in linkInfo:
                linkInfo[linkKey].append(i)
            else:
                linkInfo[linkKey] = [i]
    return linkInfo

def search_links(tree):
    return list(linkPaths_search(tree).keys())

def _gather_parameters(tree, parameters):
    indentCount = 0
    for key, value in tree.items():
        if key.startswith(KEY_PARAM+':'):
            if KEY_PARAM_INDENT == key:
                indentCount += value
            else:
                parameters[key] = value
    return indentCount

def _strip_parameter_keys(parameters):
    stripped_parameters = dict()
    for key, value in parameters.items():
        assert key.startswith(KEY_PARAM+':')
        r = re.split(r'[:\s]+', key)
        stripped_parameters[r[1]] = value
    return stripped_parameters

def _substitute_parameters_regex(line, parameters):
    if not (KEY_PARAM in line):
        return line
    for key, value in parameters.items():
        line = re.sub(r'\b'+str(key)+r'\b', str(value), line)
    return line

def _substitute_parameters(line, parameters, template_type):
    """
    Takes in three parameters:
        - line - str
        - parameters - dict
        - template_type - str
            default: "regex", changing for testing of mako and string
    The line is the string that is parsed for any keywords that will
    be replaced by the corresponding value from the parameters dictionary.
    Depending on the type given into the template type, three different substitution
    systems may be used, either a built in regex substitution system, the Python
    Template system, or the Mako system, each ends up returning the same string with replaced values.
    """
    assert isinstance(line, str), type(line)
    assert isinstance(parameters, dict), type(parameters)
    if template_type == 'regex':
        return _substitute_parameters_regex(line, parameters)
    elif template_type == 'string':
        from string import Template
        try:
            _parameters = _strip_parameter_keys(copy.deepcopy(parameters)) # TODO temporary
            string_tpl = Template(line)
            #substituted_str = string_tpl.safe_substitute(_parameters) # this makes partial substitutions
            substituted_str = string_tpl.substitute(_parameters) # this behaves like cheetah and mako
            return substituted_str
        except KeyError as e:
            print('Error: Parameter "{}" not found'.format(e))
            return line # TODO this does not substitute partially known variables
    elif template_type == 'cheetah':
        try:
            from Cheetah.Template import Template
            from Cheetah import NameMapper
        except ModuleNotFoundError:
            raise ModuleNotFoundError('Cheetah must be installed to use the Cheetah template.')
        try:
            _parameters = _strip_parameter_keys(copy.deepcopy(parameters)) # TODO temporary
            cheetah_tpl = Template.compile(line, compilerSettings=dict(directiveStartToken='//#', directiveEndToken='//#'))
            substituted_tpl = cheetah_tpl(searchList=[_parameters])
            return str(substituted_tpl)
        except NameMapper.NotFound as e:
            print('Error:', e)
            return line # TODO this does not substitute partially known variables
    elif template_type == 'mako':
        """
        Looking for method to grab all values to be changed in the template.
        """
        try:
            from mako.template import Template
        except ModuleNotFoundError:
            raise ModuleNotFoundError('Mako must be installed to use the Mako template.')
# TODO unused error catching for mako
#        def _error_handler(context, exception):
#            if isinstance(exception, NameError):
#                return True
#            return False
        try:
            _parameters = _strip_parameter_keys(copy.deepcopy(parameters)) # TODO temporary
#           mako_tpl = Template(line, error_handler=_error_handler) #TODO unused argument, todo see above
            mako_tpl = Template(line)
            substituted_str = mako_tpl.render(**_parameters)
            return substituted_str
        except NameError as e:
            print('Error:', e)
            return line # TODO this does not substitute partially known variables
    else:
        raise NotImplementedError('Template type "{}" is not supported'.format(template_type))

def _parse_line_c_fortran(line, indentSpace, indentCount):
    if re.search(r'^\s*#', line):
        # parse macros without indentation
        line = line.lstrip()
    elif '\n' in line:
        # parse string that has line breaks
        line = [indentSpace * indentCount + l.rstrip() for l in line.splitlines()]
        line = '\n'.join(line)
    else:
        # parse regular line of code
        line = indentSpace * indentCount + line
    return line.rstrip()

def _parse_line(whichType, line, indentSpace, indentCount):
    if   whichType is None:
        return indentSpace * indentCount + line
    elif whichType in C_SUFFIX or \
         whichType in FORTRAN_SUFFIX:
        return _parse_line_c_fortran(line, indentSpace, indentCount)
    else:
        raise NotImplementedError('File type "{}" is not supported'.format(whichType))

def _string_has_any_item(string, items):
    ''' Checks whether any of the strings stored in `items` is contained in
        `string`.  `items` has to be a list of str. '''
    return any([(item in string) for item in items])

def _string_has_more_plus_items(string, items_plus, items_minus):
    assert 1 == len(items_plus)  # not sure if the function is correct if not
    assert 1 == len(items_minus) # not sure if the function is correct if not
    count_items_p = sum([string.count(item) for item in items_plus])
    count_items_m = sum([string.count(item) for item in items_minus])
    return 0 < (count_items_p - count_items_m)

def _string_startswith_endswith_any_item(string, items):
    ''' Checks whether `string` starts or ends with any of the strings stored
        in `items`.  `items` has to be a list of tuples/lists with
        (startswith_str,endswith_str). '''
    s = string.lstrip()
    return any([(item[0] is not None and s.startswith(item[0])) or
                (item[1] is not None and s.endswith(item[1])) for item in items])

#########################
# Load and Dump Functions
#########################

def _load_json(path):
    assert isinstance(path, pathlib.Path), type(path)
    with open(path, 'r') as f:
        return json.load(f)
    return dict()


C_SUFFIX = ['.c', '.cc', '.cpp', '.cu']
C_INDENT_INCR = ['{']
C_INDENT_DECR = ['}']

def _load_c(path):
    assert isinstance(path, pathlib.Path), type(path)
    lines = path.read_text().splitlines()
    tree  = dict()
    # split up sections of source code
    split_indices = list()
    for i, line in enumerate(lines):
        if KEY_CONNECTOR in line:
            split_indices.append(i)
    split_indices.append(len(lines))
    if 0 != split_indices[0]:
        split_indices = [0] + split_indices
    # generate tree from source code
    for split_idx in range(len(split_indices) - 1):
        lines_split = lines[split_indices[split_idx]:split_indices[split_idx+1]]
        lineno_remove = list()
        if KEY_CONNECTOR in lines_split[0]:
            connector = re.search(r'\b'+KEY_CONNECTOR+r'[:\w]*\b', lines_split[0])
            if connector:
                connector = connector.group()
                lineno_remove.append(0)
        else:
            connector = None
        indentCount = 0
        params = dict()
        for i, line in enumerate(lines_split):
            if _string_has_more_plus_items(line, C_INDENT_INCR, C_INDENT_DECR):
                indentCount += 1
            if _string_has_more_plus_items(line, C_INDENT_DECR, C_INDENT_INCR):
                indentCount -= 1
            if re.search(r'[/\*]{2}\s*'+KEY_PARAM, line):
                matches = re.findall(r'\b'+KEY_PARAM+r':\w+\b\s*={1}\s*.*$', line)
                for m in matches:
                    s = re.split(r'\s*={1}\s*', m)
                    assert 2 <= len(s)
                    params[s[0]] = s[1].rstrip(r'*/ ').strip()
                if matches:
                    lineno_remove.append(i)
            if KEY_LINK in line:
                linkName = re.search(r'\b'+KEY_LINK+r'[:\w]*\b', line)
                if linkName:
                    linkName = linkName.group()
                    lines_split[i] = { KEY_PARAM_INDENT: indentCount, linkName: [] }
        # include trailing empty lines for removal
        lineno_trailing = list()
        for i, line in reversed(list(enumerate(lines_split))): # loop backward
            if isinstance(line, str) and not line.strip(): # if line is empty string
                if i not in lineno_remove:
                    lineno_trailing.insert(0, i)
            else:
                break
        lineno_remove += lineno_trailing
        # remove lines
        for i in reversed(lineno_remove): # loop backwards over line numbers
            lines_split.pop(i)
        # add items to tree
        if connector:
            assert isinstance(connector, str), type(connector)
            tree[connector] = {KEY_CODE: lines_split}
            tree[connector].update(params)
        else:
            tree.update({KEY_CODE: lines_split})
            tree.update(params)
    # return tree
    return tree


FORTRAN_SUFFIX = ['.f', '.f90']
FORTRAN_INDENT_INCR = [('do'    , None), ('do'   , None), (None    , 'then'), (None   , 'then'), ('module'    , None), ('subroutine'    , None)]
FORTRAN_INDENT_DECR = [('end do', None), ('enddo', None), ('end if', None  ), ('endif', None  ), ('end module', None), ('end subroutine', None)]
#TODO 'if' does not properly account for single-line if statements (without 'then')

def _load_fortran(path):
    assert isinstance(path, pathlib.Path), type(path)
    lines = path.read_text().splitlines()
    tree  = dict()
    # split up sections of source code
    split_indices = list()
    for i, line in enumerate(lines):
        if KEY_CONNECTOR in line:
            split_indices.append(i)
    split_indices.append(len(lines))
    if 0 != split_indices[0]:
        split_indices = [0] + split_indices
    # generate tree from source code
    for split_idx in range(len(split_indices) - 1):
        lines_split = lines[split_indices[split_idx]:split_indices[split_idx+1]]
        lineno_remove = list()
        if KEY_CONNECTOR in lines_split[0]:
            connector = re.search(r'\b'+KEY_CONNECTOR+r'[:\w]*\b', lines_split[0])
            if connector:
                connector = connector.group()
                lineno_remove.append(0)
        else:
            connector = None
        indentCount = 0
        params = dict()
        for i, line in enumerate(lines_split):
            if _string_startswith_endswith_any_item(line, FORTRAN_INDENT_INCR):
                indentCount += 1
            if _string_startswith_endswith_any_item(line, FORTRAN_INDENT_DECR):
                indentCount -= 1
            if re.search(r'!+\s*'+KEY_PARAM, line):
                matches = re.findall(r'\b'+KEY_PARAM+r':\w+\b\s*={1}\s*.*$', line)
                for m in matches:
                    s = re.split(r'\s*={1}\s*', m)
                    assert 2 <= len(s)
                    params[s[0]] = s[1].strip()
                if matches:
                    lineno_remove.append(i)
            if KEY_LINK in line:
                linkName = re.search(r'\b'+KEY_LINK+r'[:\w]*\b', line)
                if linkName:
                    linkName = linkName.group()
                    lines_split[i] = { KEY_PARAM_INDENT: indentCount, linkName: [] }
        # include trailing empty lines for removal
        lineno_trailing = list()
        for i, line in reversed(list(enumerate(lines_split))): # loop backward
            if isinstance(line, str) and not line.strip(): # if line is empty string
                if i not in lineno_remove:
                    lineno_trailing.insert(0, i)
            else:
                break
        lineno_remove += lineno_trailing
        # remove lines
        for i in reversed(lineno_remove): # loop backwards over line numbers
            lines_split.pop(i)
        # add items to tree
        if connector:
            assert isinstance(connector, str), type(connector)
            tree[connector] = {KEY_CODE: lines_split}
            tree[connector].update(params)
        else:
            tree.update({KEY_CODE: lines_split})
            tree.update(params)
    # return tree
    return tree


def load(path):
    ''' TODO '''
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    suffix = path.suffix.lower()
    if   suffix == '.json':  # if load JSON
        tree     = _load_json(path)
        fileType = tree.get(KEY_PARAM_TYPE, None)
    elif suffix in C_SUFFIX:  # if load C/C++ source
        tree     = _load_c(path)
        fileType = suffix
    elif suffix in FORTRAN_SUFFIX:  # if load FORTRAN source
        tree     = _load_fortran(path)
        fileType = suffix
    else:  # otherwise file is unknown
        raise NotImplementedError('File type "{}" is not supported'.format(suffix))
    # remove connectors from top layer
    #TODO there is probably no need for this top layer stuff
#   if isTopLayer:
#       items = dict()
#       for treekey in tree.keys():
#           if KEY_CONNECTOR in treekey.lower():
#               popped = tree.pop(treekey, None)
#               for key, value in popped.items():
#                   if KEY_CODE == key:
#                       try:
#                           items[key].extend(value)
#                       except KeyError:
#                           items[key] = value
#                       except:
#                           raise
#                   else:
#                       items[key] = value
#       tree.update(items)
    # add file name as parameter
    tree[KEY_PARAM_FILE] = path.name
    tree[KEY_PARAM_TYPE] = fileType
    return tree


def dump(tree, path, indentNSpaces=2):
    ''' TODO '''
    assert isinstance(tree, dict), type(tree)
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    suffix = path.suffix.lower()
    with open(path, 'w') as f:
        if suffix == '.json':
            json.dump(tree, f, indent=indentNSpaces)
        else:
            raise NotImplementedError('File type "{}" is not supported'.format(suffix))
