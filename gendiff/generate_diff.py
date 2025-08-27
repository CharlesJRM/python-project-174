from gendiff.file_reader import read_file
from gendiff.parser import parse
from gendiff.diff_calculator import build_diff

def generate_diff(file_path1, file_path2):
    content1 = read_file(file_path1)
    content2 = read_file(file_path2)
    data1 = parse(content1, file_path1)
    data2 = parse(content2, file_path2)
    return build_diff(data1, data2)
