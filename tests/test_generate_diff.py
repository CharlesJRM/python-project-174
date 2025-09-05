import os
from gendiff.generate_diff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "fixtures")


def fixtures_path(name):
    return os.path.join(os.path.dirname(__file__), "fixtures", name)


def read_file(name):
    with open(fixtures_path(name), "r", encoding="utf-8") as f:
        return f.read().strip()


def test_generate_diff_json():
    file1 = fixtures_path("file1.json")
    file2 = fixtures_path("file2.json")
    expected = read_file("expected.txt")
    assert generate_diff(file1, file2) == expected


def test_generate_diff_json_format():
    file1 = fixtures_path("file1.json")
    file2 = fixtures_path("file2.json")
    diff = generate_diff(file1, file2, "json")
    assert diff.strip().startswith("{") or diff.strip().startswith("[")


def test_generate_diff_yml():
    file1 = fixtures_path("file1.yml")
    file2 = fixtures_path("file2.yml")
    expected = read_file("expected_yml.txt")
    assert generate_diff(file1, file2) == expected


"""Convierte valores a las cadenas esperadas en stylish."""


def test_generate_diff_identical_files():
    file1 = fixtures_path("file1.json")
    assert generate_diff(file1, file1) == "{}"


def test_generate_diff_plain():
    file1 = fixtures_path("file1.json")
    file2 = fixtures_path("file2.json")
    diff = generate_diff(file1, file2, "plain")
    assert "Property" in diff  # test básico
