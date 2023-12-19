from src.Searcher import Searcher


def test_searcher():
    orange_id = "1"
    apple_id = "2"
    banana_id = "3"

    searcher = Searcher()
    result = searcher.search("apple")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([apple_id])
    result = searcher.search("orange")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([orange_id])
    result = searcher.search("banana")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([banana_id])
    result = searcher.search("NOT apple")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set(
        [orange_id, banana_id]
    )
    result = searcher.search("apple AND orange")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([])
    result = searcher.search("apple OR orange")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set(
        [apple_id, orange_id]
    )
    result = searcher.search("apple OR orange AND banana")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([apple_id])
    result = searcher.search("(apple OR orange) AND banana")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set([])
    result = searcher.search("(apple OR orange) AND NOT banana")
    assert set([hit["_id"] for hit in result["hits"]["hits"]]) == set(
        [apple_id, orange_id]
    )
