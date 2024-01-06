# Simple Search Query Parser Sample
This is an appendix to the [検索クエリパーサー自作入門](https://tech.legalforce.co.jp/entry/2023/12/20/211139) article published on the LegalOn Technologies Engineering Blog.  
  
The goal is to learn how to create a search query parser through implementation examples.

## Prerequisites
* Install Python. (^3.11)
* Running Docker daemon.
* Install Visual Studio Code and [ANTLR4 grammar syntax support](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4).

## Directory
```
.vscode              -- Settings for ANTLR4 grammar syntax support
elasticsearch        -- Elasticsearch for local use
src                  -- Source of sample programs
tests                -- Unit test
Makefile             -- Define simplified commands
```

## Query Syntax
The query syntax we will define is simple as follows.

- **Conjunctive query**  
    A search with `A AND B` will result in hits only for documents that contain both `A` and `B`.
    
- **Disjunctive query**  
    A search with `A OR B` will result in documents containing either `A` or `B`.
    
- **Negative query**  
    A search with `NOT A` will result in hits only for documents that do not contain `A`.
    
- **Compound query**  
    A query that combines multiple Conjunctive, Disjunctive, and Negative queries.
    
    - Operator priority  
        Evaluated with the precedence of the `NOT` operator, the `AND` operator, or the `OR` operator.  
        However, queries enclosed in parentheses are evaluated with priority.
        - In the case of `NOT A OR B AND C`, evaluation is performed in the order `((NOT A) OR (B AND C))`.
        - In the case of `(NOT A OR B) AND C`, evaluation is performed in the order `((NOT A) OR B) AND C)`.

The query syntax in this example implementation is defined in the BNF below.  
This grammar is an example; other ways of expression are possible.  

```
<or_operator>::= OR
<and_operator>::= AND
<not_operator>::= NOT
<expr>::= <term>|<expr><or_operator><term>
<term>::= <factor>|<term><and_operator><factor>
<factor>::= <keyword>|<not_operator><keyword>
<keyword>::= (<expr>)|<alphabets>
<alphabets>::= a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
```

## Set up

1. Install poetry
```
make install-poetry
```

If there is an executable in `~/.local/bin/poetry`, add it to the PATH.

2. Set up
```
make setup
```

## Run

3. Run Elasticsearch
```
make compose-up
```

4. Index sample documents
```
make index-documents
```

5. Run Driver1.py (Using QueryParser)
```
make run-driver1

Output:
{'operator': 'AND', 'children': [{'operator': 'OR', 'children': [{'value': 'apple'}, {'value': 'orange'}]}, {'operator': 'NOT', 'children': [{'value': 'banana'}]}]}
```

6. Run Driver2.py (Using QueryBuilder)
```
make run-driver2

Output:
{
  "query": {
    "bool": {
      "must": [
        {
          "bool": {
            "should": [
              {
                "match": {
                  "fruit": {
                    "query": "apple"
                  }
                }
              },
              {
                "match": {
                  "fruit": {
                    "query": "orange"
                  }
                }
              }
            ],
            "minimum_should_match": 1
          }
        },
        {
          "bool": {
            "must_not": [
              {
                "match": {
                  "fruit": {
                    "query": "banana"
                  }
                }
              }
            ]
          }
        }
      ]
    }
  }
}
```

7. Run Driver3.py (Using Searcher)
```
make run-driver3

Output:
{
  "took": 10,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 0.9808291,
    "hits": [
      {
        "_index": "fruit_basket",
        "_id": "1",
        "_score": 0.9808291,
        "_source": {
          "fruit": "orange"
        }
      },
      {
        "_index": "fruit_basket",
        "_id": "2",
        "_score": 0.9808291,
        "_source": {
          "fruit": "apple"
        }
      }
    ]
  }
}
```

8. test about Sercher.py
```
make test
```

## License
Licensed under either of  
  
- Apache License, Version 2.0 ([LICENSE-APACHE](https://github.com/legalontech-oss/simple-search-query-parser-sample/blob/main/LICENSE-APACHE))
- MIT license ([LICENSE-MIT](https://github.com/legalontech-oss/simple-search-query-parser-sample/blob/main/LICENSE-MIT))

at your option.  
