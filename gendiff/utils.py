def to_str(value):
    """Convierte valores a las cadenas esperadas en stylish."""
    if isinstance(value, bool):
        return str(value).lower()  # True -> true, False -> false
    if value is None:
        return "null"
    return str(value)
