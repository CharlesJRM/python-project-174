def to_str(value, depth):
    """
    Convierte un valor en su representación string para stylish.
    depth indica el nivel de profundidad (para indentación).
    """
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {to_str(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def _has_changes(diff):
    """
    Recorre el diff de forma recursiva y devuelve True si hay
    al menos un nodo 'added', 'removed' o 'changed'.
    """
    for node in diff:
        t = node["type"]
        if t in ("added", "removed", "changed"):
            return True
        if t == "nested" and _has_changes(node["children"]):
            return True
    return False


def format_stylish(diff, depth=0):
    """
    Dado el árbol 'diff' lo formatea en el estilo 'stylish'.
    Si no hay cambios en todo el árbol, devuelve '{}'.
    """
    # Si no hay ningún cambio en todo el diff, devolvemos '{}'
    if not _has_changes(diff):
        return "{}"

    indent = " " * (depth * 4)
    lines = []

    for node in diff:
        key = node["key"]
        t = node["type"]

        if t == "nested":
            children_text = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}    {key}: {children_text}")
        elif t == "unchanged":
            lines.append(
                f"{indent}  - {key}: {to_str(node['old_value'], depth + 1)}")
        elif t == "removed":
            lines.append(
                f"{indent}  - {key}: {to_str(node['value'], depth + 1)}")
        elif t == "added":
            lines.append(
                f"{indent}  + {key}: {to_str(node['value'], depth + 1)}")
        elif t == "changed":
            lines.append(
                f"{indent}  - {key}: {to_str(node['old_value'], depth + 1)}")
            lines.append(
                f"{indent}  + {key}: {to_str(node['new_value'], depth + 1)}")

    return "{\n" + "\n".join(lines) + f"\n{indent}}}"
