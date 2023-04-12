from enum import Enum
import json


class SkuSchemes(str, Enum):
    FBO = "FBO"
    FBS = "FBS"
    RETAIL = "RETAIL"


"""
Если нужно добавить несколько примеров в Response, то для этого нужно
в секции "examples" добавить еще один вложенный элемент и сделать по аналогии с "one"
"""
responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "0": {
                        "value": json.loads(open("response.json", "r").read())
                    }
                }
            }
        }
    }
}