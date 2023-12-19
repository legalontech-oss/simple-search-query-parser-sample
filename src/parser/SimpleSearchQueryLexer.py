from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,4,2,21,8,2,11,2,12,2,22,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,4,6,37,8,6,11,6,12,6,38,1,6,1,
        6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,97,122,3,0,9,10,
        13,13,32,32,43,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,
        20,1,0,0,0,7,24,1,0,0,0,9,27,1,0,0,0,11,31,1,0,0,0,13,36,1,0,0,0,
        15,16,5,40,0,0,16,2,1,0,0,0,17,18,5,41,0,0,18,4,1,0,0,0,19,21,7,
        0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,
        6,1,0,0,0,24,25,5,79,0,0,25,26,5,82,0,0,26,8,1,0,0,0,27,28,5,65,
        0,0,28,29,5,78,0,0,29,30,5,68,0,0,30,10,1,0,0,0,31,32,5,78,0,0,32,
        33,5,79,0,0,33,34,5,84,0,0,34,12,1,0,0,0,35,37,7,1,0,0,36,35,1,0,
        0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,
        6,6,0,0,41,14,1,0,0,0,3,0,22,38,1,6,0,0
    ]

class SimpleSearchQueryLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ALPHABETS = 3
    OR_OPERATOR = 4
    AND_OPERATOR = 5
    NOT_OPERATOR = 6
    WHITE_SPACES = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'OR'", "'AND'", "'NOT'" ]

    symbolicNames = [ "<INVALID>",
            "ALPHABETS", "OR_OPERATOR", "AND_OPERATOR", "NOT_OPERATOR", 
            "WHITE_SPACES" ]

    ruleNames = [ "T__0", "T__1", "ALPHABETS", "OR_OPERATOR", "AND_OPERATOR", 
                  "NOT_OPERATOR", "WHITE_SPACES" ]

    grammarFileName = "SimpleSearchQuery.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


