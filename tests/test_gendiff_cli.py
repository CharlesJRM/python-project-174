import subprocess
import json
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent / "fixtures"
FILE1_JSON = FIXTURES_DIR / "file1.json"
FILE2_JSON = FIXTURES_DIR / "file2.json"
FILE1_YML = FIXTURES_DIR / "file1.yml"
FILE2_YML = FIXTURES_DIR / "file2.yml"


def run_cli(*args):
    """Ejecuta la CLI usando poetry run python -m gendiff.scripts.gendiff."""
    result = subprocess.run(
        ["poetry", "run", "python", "-m", "gendiff.scripts.gendiff", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    assert result.returncode == 0, (
        f"Error en CLI: {result.stderr or 'sin salida de error'}"
    )
    return result.stdout.strip()


def test_cli_stylish_json_files():
    output = run_cli(str(FILE1_JSON), str(FILE2_JSON), "--format", "stylish")
    assert isinstance(output, str)
    assert "host" in output or "timeout" in output


def test_cli_json_format():
    output = run_cli(str(FILE1_JSON), str(FILE2_JSON), "--format", "json")
    parsed = json.loads(output)
    assert isinstance(parsed, (list, dict))


def test_cli_stylish_yml_files():
    output = run_cli(str(FILE1_YML), str(FILE2_YML), "--format", "stylish")
    assert isinstance(output, str)
    assert "host" in output or "timeout" in output
