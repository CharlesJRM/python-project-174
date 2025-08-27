import argparse
from .parser import parse

def main():
    parser = argparse.ArgumentParser(description="Herramienta para parsear archivos JSON/YAML")
    parser.add_argument("file", help="Ruta al archivo a parsear")
    args = parser.parse_args()

    # Leer contenido
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    # Parsear según extensión
    try:
        data = parse(content, args.file)
        print("Contenido parseado correctamente:")
        print(data)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
