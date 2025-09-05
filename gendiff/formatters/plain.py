def format_plain(diff):
    lines = []

    def walk(node, path=""):
        for item in node:
            key = item["key"]
            property_path = f"{path}.{key}" if path else key
            node_type = item["type"]

            if node_type == "nested":
                walk(item["children"], property_path)
            elif node_type == "added":
                value = stringify(item["value"])
                lines.append(
                    f"Property '{property_path}' was added with value: {value}"
                    )
            elif node_type == "removed":
                lines.append(f"Property '{property_path}' was removed")
            elif node_type == "changed":
                old_value = stringify(item["old_value"])
                new_value = stringify(item["new_value"])
                lines.append(
                    f"Property '{property_path}' was updated."
                    f"From {old_value} to {new_value}"
                )
            # unchanged no se muestra en formato plain

    walk(diff)
    return "\n".join(lines)


def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)
