import sys

from antlr4 import CommonTokenStream, FileStream

from src.parser.SimpleSearchQueryLexer import SimpleSearchQueryLexer
from src.parser.SimpleSearchQueryParser import SimpleSearchQueryParser
from src.VisitorInterp import VisitorInterp


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SimpleSearchQueryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleSearchQueryParser(stream)
    tree = parser.expr()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        print(vinterp.visit(tree))


if __name__ == "__main__":
    main(sys.argv)
