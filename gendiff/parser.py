import json
import yaml
import os

def parse(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as file:
        content = file.read()

    if ext in ('.yaml', '.yml'):
        return yaml.safe_load(content)
    elif ext == '.json':
        return json.loads(content)
    else:
        raise ValueError(f'Formato de archivo no soportado: {ext}')
