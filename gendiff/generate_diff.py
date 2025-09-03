import json
import yaml
from gendiff.utils import to_str


def parse_file(path):
    """Detecta el formato según la extensión y carga como dict."""
    if path.endswith(('.yml', '.yaml')):
        with open(path) as f:
            return yaml.safe_load(f)
    with open(path) as f:
        return json.load(f)


def generate_diff(file_path1, file_path2):
    dict1 = parse_file(file_path1)
    dict2 = parse_file(file_path2)

    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff_lines = ['{']
    changes_found = False

    for key in keys:
        if key in dict1 and key not in dict2:
            changes_found = True
            diff_lines.append(f"  - {key}: {to_str(dict1[key])}")
        elif key not in dict1 and key in dict2:
            changes_found = True
            diff_lines.append(f"  + {key}: {to_str(dict2[key])}")
        elif dict1[key] == dict2[key]:
            diff_lines.append(f"    {key}: {to_str(dict1[key])}")
        else:
            changes_found = True
            diff_lines.append(f"  - {key}: {to_str(dict1[key])}")
            diff_lines.append(f"  + {key}: {to_str(dict2[key])}")

    diff_lines.append('}')
    if not changes_found:
        return "{}"
    return '\n'.join(diff_lines)

def build_diff(dict1, dict2):
    """Construye recursivamente el árbol de diferencias entre dos dicts."""
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff = []

    for key in keys:
        in1 = key in dict1
        in2 = key in dict2

        if in1 and not in2:
            diff.append({
                "key": key,
                "type": "removed",
                "old_value": dict1[key],
            })
        elif not in1 and in2:
            diff.append({
                "key": key,
                "type": "added",
                "old_value": dict2[key],  # stylish espera 'old_value'
            })
        else:
            v1 = dict1[key]
            v2 = dict2[key]
            if isinstance(v1, dict) and isinstance(v2, dict):
                diff.append({
                    "key": key,
                    "type": "nested",
                    "children": build_diff(v1, v2)
                })
            elif v1 == v2:
                diff.append({
                    "key": key,
                    "type": "unchanged",
                    "old_value": v1,  # stylish espera 'old_value'
                })
            else:
                diff.append({
                    "key": key,
                    "type": "changed",
                    "old_value": v1,
                    "new_value": v2
                })

    return diff
