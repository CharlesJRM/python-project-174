from .generate_diff import generate_diff

__all__ = ["generate_diff"]

from gendiff import generate_diff

print(generate_diff("file1.json", "file2.json"))
