import json
from gendiff.utils import to_str


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        dict1 = json.load(f1)
        dict2 = json.load(f2)

    diff = ['{']
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    for key in keys:
        if key in dict1 and key not in dict2:
            diff.append(f"  - {key}: {to_str(dict1[key])}")
        elif key not in dict1 and key in dict2:
            diff.append(f"  + {key}: {to_str(dict2[key])}")
        elif dict1[key] == dict2[key]:
            diff.append(f"    {key}: {to_str(dict1[key])}")
        else:
            diff.append(f"  - {key}: {to_str(dict1[key])}")
            diff.append(f"  + {key}: {to_str(dict2[key])}")
    diff.append('}')
    return '\n'.join(diff)
