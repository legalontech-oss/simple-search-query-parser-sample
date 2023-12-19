# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,0,
        1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        28,8,1,10,1,12,1,31,9,1,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,
        3,3,3,43,8,3,1,4,1,4,1,4,0,2,0,2,5,0,2,4,6,8,0,0,45,0,10,1,0,0,0,
        2,21,1,0,0,0,4,35,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,11,6,0,-1,
        0,11,12,3,2,1,0,12,18,1,0,0,0,13,14,10,1,0,0,14,15,5,4,0,0,15,17,
        3,2,1,0,16,13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,
        19,1,1,0,0,0,20,18,1,0,0,0,21,22,6,1,-1,0,22,23,3,4,2,0,23,29,1,
        0,0,0,24,25,10,1,0,0,25,26,5,5,0,0,26,28,3,4,2,0,27,24,1,0,0,0,28,
        31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,29,1,0,0,
        0,32,36,3,6,3,0,33,34,5,6,0,0,34,36,3,6,3,0,35,32,1,0,0,0,35,33,
        1,0,0,0,36,5,1,0,0,0,37,38,5,1,0,0,38,39,3,0,0,0,39,40,5,2,0,0,40,
        43,1,0,0,0,41,43,3,8,4,0,42,37,1,0,0,0,42,41,1,0,0,0,43,7,1,0,0,
        0,44,45,5,3,0,0,45,9,1,0,0,0,4,18,29,35,42
    ]

class SimpleSearchQueryParser ( Parser ):

    grammarFileName = "SimpleSearchQuery.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'OR'", "'AND'", 
                     "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ALPHABETS", 
                      "OR_OPERATOR", "AND_OPERATOR", "NOT_OPERATOR", "WHITE_SPACES" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_keywords = 3
    RULE_alphabets = 4

    ruleNames =  [ "expr", "term", "factor", "keywords", "alphabets" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ALPHABETS=3
    OR_OPERATOR=4
    AND_OPERATOR=5
    NOT_OPERATOR=6
    WHITE_SPACES=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.ExprContext,0)


        def OR_OPERATOR(self):
            return self.getToken(SimpleSearchQueryParser.OR_OPERATOR, 0)

        def getRuleIndex(self):
            return SimpleSearchQueryParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleSearchQueryParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleSearchQueryParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 13
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 14
                    self.match(SimpleSearchQueryParser.OR_OPERATOR)
                    self.state = 15
                    self.term(0) 
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.TermContext,0)


        def AND_OPERATOR(self):
            return self.getToken(SimpleSearchQueryParser.AND_OPERATOR, 0)

        def getRuleIndex(self):
            return SimpleSearchQueryParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleSearchQueryParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleSearchQueryParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 24
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 25
                    self.match(SimpleSearchQueryParser.AND_OPERATOR)
                    self.state = 26
                    self.factor() 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keywords(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.KeywordsContext,0)


        def NOT_OPERATOR(self):
            return self.getToken(SimpleSearchQueryParser.NOT_OPERATOR, 0)

        def getRuleIndex(self):
            return SimpleSearchQueryParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = SimpleSearchQueryParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.keywords()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(SimpleSearchQueryParser.NOT_OPERATOR)
                self.state = 34
                self.keywords()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.ExprContext,0)


        def alphabets(self):
            return self.getTypedRuleContext(SimpleSearchQueryParser.AlphabetsContext,0)


        def getRuleIndex(self):
            return SimpleSearchQueryParser.RULE_keywords

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywords" ):
                return visitor.visitKeywords(self)
            else:
                return visitor.visitChildren(self)




    def keywords(self):

        localctx = SimpleSearchQueryParser.KeywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_keywords)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(SimpleSearchQueryParser.T__0)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(SimpleSearchQueryParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.alphabets()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlphabetsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHABETS(self):
            return self.getToken(SimpleSearchQueryParser.ALPHABETS, 0)

        def getRuleIndex(self):
            return SimpleSearchQueryParser.RULE_alphabets

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlphabets" ):
                return visitor.visitAlphabets(self)
            else:
                return visitor.visitChildren(self)




    def alphabets(self):

        localctx = SimpleSearchQueryParser.AlphabetsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alphabets)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SimpleSearchQueryParser.ALPHABETS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        self._predicates[1] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




