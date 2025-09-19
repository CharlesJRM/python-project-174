def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })
        elif key not in data1:
            diff.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })
        else:
            val1 = data1[key]
            val2 = data2[key]
            if isinstance(val1, dict) and isinstance(val2, dict):
                diff.append({
                    "key": key,
                    "type": "nested",
                    "children": build_diff(val1, val2)
                })
            elif val1 == val2:
                diff.append({
                    "key": key,
                    "type": "unchanged",
                    "value": val1
                })
            else:
                diff.append({
                    "key": key,
                    "type": "changed",
                    "old_value": val1,
                    "new_value": val2
                })
    return diff
