import json

def format_json(diff):
    """Convierte el árbol de diferencias en JSON con indentación."""
    return json.dumps(diff, indent=4, ensure_ascii=False)
