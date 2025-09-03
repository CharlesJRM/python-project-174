def to_str(value):
    """Convierte valores a string estilo JSON (true/false/null en minúsculas)."""
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)
