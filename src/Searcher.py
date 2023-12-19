from antlr4 import CommonTokenStream, InputStream
from elasticsearch import Elasticsearch

from src.parser.SimpleSearchQueryLexer import SimpleSearchQueryLexer
from src.parser.SimpleSearchQueryParser import SimpleSearchQueryParser
from src.QueryBuilder import QueryBuilder
from src.VisitorInterp import VisitorInterp


class Searcher:
    def __init__(
        self, endpoint: str = "http://localhost:9200", index: str = "fruit_basket"
    ):
        self.es_client = Elasticsearch([endpoint])
        self.index = index
        self.vinterp = VisitorInterp()
        self.query_builder = QueryBuilder()

    def search(self, search_query: str) -> dict:
        input_stream = InputStream(search_query)
        lexer = SimpleSearchQueryLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SimpleSearchQueryParser(stream)
        tree = parser.expr()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise ValueError("syntax errors")
        else:
            ast = self.vinterp.visit(tree)
            es_query = self.query_builder.build(ast)
            return self.es_client.search(
                index=self.index,
                **es_query,
            ).body
