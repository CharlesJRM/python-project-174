def generate_diff(dict1, dict2, parent_key=""):
    """
    Compara dos diccionarios y devuelve una lista de diferencias.
    """
    diffs = []

    # Todas las claves de ambos diccionarios
    keys = set(dict1.keys()) | set(dict2.keys())

    for key in sorted(keys):
        full_key = f"{parent_key}.{key}" if parent_key else key

        if key not in dict1:
            diffs.append(f"Se agregó '{full_key}' con valor: {dict2[key]!r}")
        elif key not in dict2:
            diffs.append(f"Se eliminó '{full_key}'")
        else:
            val1 = dict1[key]
            val2 = dict2[key]

            # Si ambos son diccionarios, comparar recursivamente
            if isinstance(val1, dict) and isinstance(val2, dict):
                diffs.extend(generate_diff(val1, val2, full_key))
            # Si son diferentes, agregar actualización
            elif val1 != val2:
                diffs.append(f"Se actualizó '{full_key}'. Antes: {val1!r}, ahora: {val2!r}")

    return diffs
