def build_diff(data1, data2):
    """
    Construye la representación 'stylish' de diferencias entre dos dicts planos.
    Reglas:
      - Claves ordenadas alfabéticamente
      - '  -' clave removida (o cambiada respecto al 2do archivo)
      - '  +' clave agregada (o nuevo valor en el 2do archivo)
      - '   ' clave sin cambios
    """
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = ["{"]

    def format_value(value):
        if isinstance(value, bool):
            return "true" if value else "false"
        if value is None:
            return "null"
        # Para este paso (archivos planos), imprimimos str() sin comillas
        return str(value)

    for key in keys:
        in1 = key in data1
        in2 = key in data2

        if in1 and not in2:
            # Eliminado
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif not in1 and in2:
            # Agregado
            lines.append(f"  + {key}: {format_value(data2[key])}")
        else:
            v1 = data1[key]
            v2 = data2[key]
            if v1 == v2:
                # Sin cambios
                lines.append(f"    {key}: {format_value(v1)}")
            else:
                # Cambiado
                lines.append(f"  - {key}: {format_value(v1)}")
                lines.append(f"  + {key}: {format_value(v2)}")

    lines.append("}")
    return "\n".join(lines)
