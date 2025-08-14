import argparse
from gendiff.file_reader import read_file
from gendiff.diff_calculator import generate_diff

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    
    # Argumentos posicionales
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    
    # Argumento opcional --format
    parser.add_argument(
        "-f", "--format",
        default="stylish",  # formato por defecto
        help="set format of output"
    )

    args = parser.parse_args()

    # Leer archivos
    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)

    # Generar diferencias
    diffs = generate_diff(data1, data2)

    # Imprimir diferencias (por ahora ignoramos el formato)
    if diffs:
        for line in diffs:
            print(line)
    else:
        print("No se encontraron diferencias")

if __name__ == "__main__":
    main()
