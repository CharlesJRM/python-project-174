import json


def generate_diff(file_path1, file_path2):
    # Leer los archivos
    with open(file_path1) as f1:
        data1 = json.load(f1)
    with open(file_path2) as f2:
        data2 = json.load(f2)

    # Construir conjunto de todas las claves
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    # Generar el diff línea por línea
    diff_lines = ["{"]
    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {data1[key]}")
        else:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")
    diff_lines.append("}")

    return "\n".join(diff_lines)
