import json


def format_json(diff):
    return json.dumps(diff, indent=2, ensure_ascii=False)


def normalize(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def format_value(value):
    if isinstance(value, dict):
        return {k: format_value(v) for k, v in value.items()}
    return normalize(value)
