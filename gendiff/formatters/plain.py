def format_plain(diff):
    """Formatea el árbol 'diff' en texto plano legible."""
    lines = []

    def walk(nodes, path=""):
        for node in nodes:
            key = node["key"]
            prop = f"{path}.{key}" if path else key
            t = node["type"]

            if t == "nested":
                walk(node["children"], prop)
            elif t == "added":
                value = stringify(node["value"])
                lines.append(
                    f"Property '{prop}' was added with value: {value}"
                )
            elif t == "removed":
                lines.append(f"Property '{prop}' was removed")
            elif t == "changed":
                old = stringify(node["old_value"])
                new = stringify(node["new_value"])
                lines.append(
                    f"Property '{prop}' was updated. From {old} to {new}"
                )
            # 'unchanged' no se muestra en formato plain

    walk(diff)
    return "\n".join(lines)


def stringify(value):
    """Convierte valores a la representación esperada en 'plain'."""
    if isinstance(value, dict):
        return "[complex value]"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
