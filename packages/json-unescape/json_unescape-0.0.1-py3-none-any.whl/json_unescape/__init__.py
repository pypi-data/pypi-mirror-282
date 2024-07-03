import json


def escape_json(json_str: str) -> str:
    nested_object: dict = {"key": json_str}
    return json.dumps(nested_object)

def unescape_json(json_str: str) -> str:
    nested_json_string: str = '{"key": ' + json_str + '}'
    return json.loads(nested_json_string)["key"]
