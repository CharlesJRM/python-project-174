import argparse


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
    # Por ahora, solo imprimimos los argumentos para verificar
    print(f"Archivo 1: {args.first_file}")
    print(f"Archivo 2: {args.second_file}")
    print(f"Formato: {args.format}")

if __name__ == "__main__":
    main()
