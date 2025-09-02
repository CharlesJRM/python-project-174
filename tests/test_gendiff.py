from gendiff.generate_diff import generate_diff


def normalize_diff(diff):
    """Quita espacios extras para que la comparación sea más flexible."""
    return [line.strip() for line in diff.splitlines() if line.strip()]


def test_gendiff_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected_file = 'tests/fixtures/expected.txt'

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(file1, file2)
    # Aquí comparamos con el contenido del archivo, no con la ruta
    assert normalize_diff(result) == normalize_diff(expected)
