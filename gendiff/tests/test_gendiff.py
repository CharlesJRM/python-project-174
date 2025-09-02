import os
from gendiff import generate_diff

def test_gendiff_json():
    # Ubicación de los fixtures
    base_path = os.path.join(os.path.dirname(__file__), "fixtures")
    file1 = os.path.join(base_path, "file1.json")
    file2 = os.path.join(base_path, "file2.json")
    expected_path = os.path.join(base_path, "expected.txt")

    with open(expected_path) as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2).strip()
    assert result == expected
