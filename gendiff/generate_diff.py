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