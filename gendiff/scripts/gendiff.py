import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compara dos archivos en sus configuracion y muestra la diferencia."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument(
        "-f", "--format",
        help="set format of output (stylish, plain, or json)",
        default="stylish"
    )

    args = parser.parse_args()
    output = generate_diff(args.first_file, args.second_file, args.format)
    print(output)


if __name__ == "__main__":
    main()
