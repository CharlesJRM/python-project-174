import argparse
from gendiff.generate_diff import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Calculadora de diferencias')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)  # temporalmente imprime la estructura raw

if __name__ == '__main__':
    main()
