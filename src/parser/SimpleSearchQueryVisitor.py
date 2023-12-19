from antlr4 import *
if "." in __name__:
    from .SimpleSearchQueryParser import SimpleSearchQueryParser
else:
    from SimpleSearchQueryParser import SimpleSearchQueryParser

# This class defines a complete generic visitor for a parse tree produced by SimpleSearchQueryParser.

class SimpleSearchQueryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleSearchQueryParser#expr.
    def visitExpr(self, ctx:SimpleSearchQueryParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSearchQueryParser#term.
    def visitTerm(self, ctx:SimpleSearchQueryParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSearchQueryParser#factor.
    def visitFactor(self, ctx:SimpleSearchQueryParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSearchQueryParser#keywords.
    def visitKeywords(self, ctx:SimpleSearchQueryParser.KeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleSearchQueryParser#alphabets.
    def visitAlphabets(self, ctx:SimpleSearchQueryParser.AlphabetsContext):
        return self.visitChildren(ctx)



del SimpleSearchQueryParser