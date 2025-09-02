import argparse
import json

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f", "--format",
        help="set format of output"
    )

    args = parser.parse_args()

    # Leer archivos JSON
    with open(args.first_file) as f1:
        data1 = json.load(f1)
    with open(args.second_file) as f2:
        data2 = json.load(f2)

    # Mostrar contenido (temporal para verificar)
    print("Contenido del primer archivo:")
    print(data1)
    print("\nContenido del segundo archivo:")
    print(data2)
    print(f"\nFormato seleccionado: {args.format}")

if __name__ == "__main__":
    main()
