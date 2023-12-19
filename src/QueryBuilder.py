class QueryBuilder:
    def build(self, ast: dict) -> dict:
        return {"query": self.build_bool_query(ast)}

    def build_bool_query(self, ast: dict) -> dict:
        operator = ast.get("operator")
        if operator:
            match operator:
                case "AND":
                    return {
                        "bool": {
                            "must": [
                                self.build_bool_query(ast["children"][0]),
                                self.build_bool_query(ast["children"][1]),
                            ]
                        }
                    }
                case "OR":
                    return {
                        "bool": {
                            "should": [
                                self.build_bool_query(ast["children"][0]),
                                self.build_bool_query(ast["children"][1]),
                            ],
                            "minimum_should_match": 1,
                        },
                    }
                case "NOT":
                    return {
                        "bool": {
                            "must_not": [
                                self.build_bool_query(ast["children"][0]),
                            ],
                        }
                    }
        else:
            return {
                "match": {
                    "fruit": {
                        "query": ast["value"],
                    }
                }
            }
