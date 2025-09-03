import json
import yaml
from gendiff.utils import to_str
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json

def generate_diff(file_path1, file_path2, format_name="stylish"):
    dict1 = parse_file(file_path1)
    dict2 = parse_file(file_path2)
    diff = build_diff(dict1, dict2)

    if format_name == "stylish":
        return format_stylish(diff)
    elif format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def parse_file(path):
    """Detecta el formato según la extensión y carga como dict."""
    if path.endswith(('.yml', '.yaml')):
        with open(path) as f:
            return yaml.safe_load(f)
    with open(path) as f:
        return json.load(f)


def build_diff(dict1, dict2):
    """Construye el árbol de diferencias entre dos diccionarios."""
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff = []

    for key in keys:
        if key not in dict2:
            diff.append({"key": key, "type": "removed", "value": dict1[key]})
        elif key not in dict1:
            diff.append({"key": key, "type": "added", "value": dict2[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({
                "key": key,
                "type": "nested",
                "children": build_diff(dict1[key], dict2[key])
            })
        elif dict1[key] == dict2[key]:
            diff.append({"key": key, "type": "unchanged", "value": dict1[key]})
        else:
            diff.append({
                "key": key,
                "type": "changed",
                "old_value": dict1[key],
                "new_value": dict2[key]
            })

    return diff
