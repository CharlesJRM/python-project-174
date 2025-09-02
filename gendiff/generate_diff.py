import json


def format_value(value):
    """Formatea valores para que coincidan con JSON (true/false para bool)."""
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    # Leer archivos JSON
    with open(file_path1) as f1:
        data1 = json.load(f1)
    with open(file_path2) as f2:
        data2 = json.load(f2)

    # Todas las claves únicas ordenadas
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_lines = ["{"]
    for key in all_keys:
        val1 = format_value(data1[key]) if key in data1 else None
        val2 = format_value(data2[key]) if key in data2 else None

        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {val1}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {val2}")
        elif val1 == val2:
            diff_lines.append(f"    {key}: {val1}")
        else:
            diff_lines.append(f"  - {key}: {val1}")
            diff_lines.append(f"  + {key}: {val2}")
    diff_lines.append("}")

    return "\n".join(diff_lines)
