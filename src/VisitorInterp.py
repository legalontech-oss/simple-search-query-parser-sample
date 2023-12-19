from src.parser.SimpleSearchQueryParser import SimpleSearchQueryParser
from src.parser.SimpleSearchQueryVisitor import SimpleSearchQueryVisitor


class VisitorInterp(SimpleSearchQueryVisitor):
    def visitExpr(self, ctx: SimpleSearchQueryParser.ExprContext):
        if ctx.getChildCount() == 3:
            opc = ctx.getChild(1).getText()
            v1 = self.visit(ctx.getChild(0))
            v2 = self.visit(ctx.getChild(2))
            return {"operator": opc, "children": [v1, v2]}
        else:
            return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx: SimpleSearchQueryParser.TermContext):
        if ctx.getChildCount() == 3:
            opc = ctx.getChild(1).getText()
            v1 = self.visit(ctx.getChild(0))
            v2 = self.visit(ctx.getChild(2))
            return {"operator": opc, "children": [v1, v2]}
        else:
            return self.visit(ctx.getChild(0))

    def visitFactor(self, ctx: SimpleSearchQueryParser.FactorContext):
        if ctx.getChildCount() == 2:
            opc = ctx.getChild(0).getText()
            v1 = self.visit(ctx.getChild(1))
            return {"operator": opc, "children": [v1]}
        else:
            return self.visit(ctx.getChild(0))

    def visitKeywords(self, ctx: SimpleSearchQueryParser.KeywordsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))
        else:
            return self.visit(ctx.getChild(0))

    def visitAlphabets(self, ctx: SimpleSearchQueryParser.AlphabetsContext):
        return {"value": ctx.getText()}
