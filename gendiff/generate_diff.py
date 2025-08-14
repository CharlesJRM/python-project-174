from gendiff.parser import parse

def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    return _build_diff(data1, data2)

def _build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for key in keys:
        if key not in data1:
            diff.append(('added', key, data2[key]))
        elif key not in data2:
            diff.append(('removed', key, data1[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append(('nested', key, _build_diff(data1[key], data2[key])))
        elif data1[key] != data2[key]:
            diff.append(('changed', key, data1[key], data2[key]))
        else:
            diff.append(('unchanged', key, data1[key]))
    return diff
