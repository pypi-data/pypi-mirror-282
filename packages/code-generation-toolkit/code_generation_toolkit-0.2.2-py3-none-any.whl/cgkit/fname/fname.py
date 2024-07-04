import re


class FunctionName():
    def __init__(self, definitions=dict(), baseSeparator='__', attributeSeparator='_', valueSeparator='', enable_debug=False, **kwargs):
        assert isinstance(enable_debug, bool), type(enable_debug)
        self._p_setSeparators(baseSeparator, attributeSeparator, valueSeparator)
        self._p_setDefinitions(definitions, **kwargs)
        self._p_setDefinitionsKeyRegex()
        self.enable_debug = enable_debug
        if self.enable_debug:  print('[FunctionName] All variables:', str(self.__dict__))

    def __str__(self):
        if self.enable_debug:  return str(self.__class__) + ':' + str(self.__dict__)
        else:                  return str(self.__class__)

    def _p_setDefinitions(self, definitions=dict(), **kwargs):
        assert isinstance(definitions, dict), type(definitions)
        # copy all definitions
        self.definitions = definitions.copy()
        self.definitions.update(kwargs)
        # convert values to sets
        for key, val in self.definitions.items():
            if   isinstance(val, set):   continue
            elif isinstance(val, str):   self.definitions[key] = set({val})
            elif isinstance(val, list):  self.definitions[key] = set(val)
            else:                        raise TypeError('Type {} is not supported'.format(type(val)))

    def _p_setDefinitionsKeyRegex(self):
        # compile regex pattern for definition keys
        pattern = r'^({}){}'.format('|'.join(self.definitions.keys()), self.valueSeparator)
        self.definitionKeysRegex = re.compile(pattern)

    def _p_setSeparators(self, baseSeparator, attributeSeparator, valueSeparator):
        assert isinstance(baseSeparator, str), type(baseSeparator)
        assert isinstance(attributeSeparator, str), type(attributeSeparator)
        assert isinstance(valueSeparator, str), type(valueSeparator)
        self.baseSeparator      = baseSeparator
        self.attributeSeparator = attributeSeparator
        self.valueSeparator     = valueSeparator

    def updateDefinitions(self, definitions=dict(), **kwargs):
        self._p_setDefinitions(definitions, **kwargs)
        self._p_setDefinitionsKeyRegex()

    def updateSeparators(self, baseSeparator=None, attributeSeparator=None, valueSeparator=None):
        if baseSeparator is None:
            baseSeparator = self.baseSeparator
        if attributeSeparator is None:
            attributeSeparator= self.attributeSeparator
        if valueSeparator is None:
            valueSeparator = self.valueSeparator
        self._p_setSeparators(baseSeparator, attributeSeparator, valueSeparator)
        self._p_setDefinitionsKeyRegex()

    def __call__(self, basename, attributes=dict(), **kwargs):
        return self.getFname(basename, attributes, **kwargs)

    def _p_getDefinitionKey(self, attributeValue):
        assert isinstance(attributeValue, str), type(attributeValue)
        for defKey, defSet in self.definitions.items():
            if attributeValue == defKey or attributeValue in defSet:
                return defKey
        return None

    def getFname(self, basename, attributes=dict(), **kwargs):
        assert isinstance(basename, str), type(basename)
        assert isinstance(attributes, dict), type(attributes)
        # gather all attributes from arguments
        attributesIn = attributes.copy()
        attributesIn.update(kwargs)
        if self.enable_debug:  print('[FunctionName.getFname] attributesIn:', attributesIn)
        # pick out only attributes that are contained in definitions
        attributesOut = dict()
        for key, val in attributesIn.items():
            defKey = self._p_getDefinitionKey(str(key))
            if defKey is not None:
                attributesOut[defKey] = str(val)
        if self.enable_debug:  print('[FunctionName.getFname] attributesOut:', attributesOut)
        # construct and return function name
        if 0 == len(attributesOut):
            name = basename
        else:
            attributeStrings = [self.valueSeparator.join(a) for a in attributesOut.items()]
            if self.enable_debug:  print('[FunctionName.getFname] attributeStrings:', attributeStrings)
            name = basename + self.baseSeparator + self.attributeSeparator.join(attributeStrings)
        if self.enable_debug:  print('[FunctionName.getFname] name:', name)
        return name

    def _p_splitName(self, name : str):
        assert isinstance(name, str), type(name)
        # split name using base separator
        splitting = name.split(self.baseSeparator)
        # separate out last item in splitting
        if 1 < len(splitting):
            return self.baseSeparator.join(splitting[:-1]), splitting[-1]
        else:
            return name, None

    def _p_splitAttributes(self, attribName : str):
        assert isinstance(attribName, str), type(attribName)
        splitting = attribName.split(self.attributeSeparator)
        return splitting

    def _p_validDefinitionKeys(self, attributeStrings : list):
        assert isinstance(attributeStrings, list), type(attributeStrings)
        return all( a.startswith(tuple(self.definitions.keys())) for a in attributeStrings )

    def _p_parseAttributes(self, attributeStrings : list):
        assert isinstance(attributeStrings, list), type(attributeStrings)
        attributes = dict()
        for a in attributeStrings:
            m = self.definitionKeysRegex.match(a)
            if m is not None:
                k = m.group(1) # get match from the first paranthesis in pattern
                attributes[k] = a[(len(k)+len(self.valueSeparator)):]
        return attributes

    def getBase(self, name : str):
        assert isinstance(name, str), type(name)
        if self.enable_debug:  print('[FunctionName.getBase] name:', name)
        # split name into (candidate) basename and attributes string
        base, attrib = self._p_splitName(name)
        if self.enable_debug:  print('[FunctionName.getBase] splitting:', base, '|', attrib)
        # check attributes string
        if attrib is not None and not self._p_validDefinitionKeys(self._p_splitAttributes(attrib)):
            # if string has invalid definition keys, join attributes string back to base
            base = base + self.baseSeparator + attrib
        if self.enable_debug:  print('[FunctionName.getBase] base:', base)
        return base

    def getAttributes(self, name : str):
        assert isinstance(name, str), type(name)
        if self.enable_debug:  print('[FunctionName.getAttributes] name:', name)
        # split name into (candidate) basename and attributes string
        base, attrib = self._p_splitName(name)
        # return if nothing to do
        if attrib is None or not self._p_validDefinitionKeys(self._p_splitAttributes(attrib)):
            if self.enable_debug:  print('[FunctionName.getAttributes] splitting:', base, '|', attrib)
            return None
        # split attributes
        attributeStrings = self._p_splitAttributes(attrib)
        attributes       = self._p_parseAttributes(attributeStrings)
        if self.enable_debug:  print('[FunctionName.getAttributes] splitting:', base, '|', attributes)
        return attributes
