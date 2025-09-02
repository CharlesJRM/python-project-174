import os
from gendiff import generate_diff


def test_gendiff_yml():
    base_path = os.path.join(os.path.dirname(__file__), "fixtures")
    file1 = os.path.join(base_path, "file1.yml")
    file2 = os.path.join(base_path, "file2.yml")
    expected_path = os.path.join(base_path, "expected_yml.txt")

    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2).strip()
    assert result == expected
