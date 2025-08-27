import json
import yaml
from pathlib import Path

def parse(content, file_path):
    """
    Parsea contenido en formato JSON o YAML.

    :param content: Texto del archivo.
    :param file_path: Ruta al archivo (para detectar extensión).
    :return: Objeto Python con el contenido parseado.
    """
    ext = Path(file_path).suffix.lower()
    if ext == ".json":
        return json.loads(content)
    elif ext in (".yml", ".yaml"):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Formato no soportado: {ext}")
