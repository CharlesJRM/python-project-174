import json
import yaml
from pathlib import Path

def read_file(file_path):
    """
    Lee un archivo JSON o YAML y devuelve un diccionario.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

    # Leer contenido del archivo
    with open(file_path, "r", encoding="utf-8") as f:
        if path.suffix in [".yaml", ".yml"]:
            return yaml.safe_load(f)
        elif path.suffix == ".json":
            return json.load(f)
        else:
            raise ValueError("Formato no soportado. Solo JSON o YAML.")


import json
import yaml
from pathlib import Path

def read_file(file_path):
    ext = Path(file_path).suffix.lower()
    with open(file_path) as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Formato no soportado: {ext}")
