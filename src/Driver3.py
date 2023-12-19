import json
import sys

from src.Searcher import Searcher

if __name__ == "__main__":
    argv = sys.argv
    input_filename = argv[1]
    with open(input_filename) as f:
        search_query = f.readline()
    searcher = Searcher()
    result = searcher.search(search_query)
    print(json.dumps(result))
