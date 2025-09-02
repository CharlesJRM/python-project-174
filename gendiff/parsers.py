import json
import os

try:
    import yaml
except Exception:  # si no está instalado, avisamos al usarlo
    yaml = None


def parse_file(file_path):
    """
    Detecta formato por extensión y devuelve un diccionario
    para JSON (.json) y YAML (.yml, .yaml).
    """
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, "r", encoding="utf-8") as f:
        if ext == ".json":
            return json.load(f)
        if ext in (".yml", ".yaml"):
            if yaml is None:
                raise RuntimeError(
                    "PyYAML no está instalado. Ejecuta: poetry add pyyaml"
                )
            return yaml.safe_load(f)
    raise ValueError(f"Unsupported file extension: {ext}")
