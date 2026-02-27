# tests/integration/test_my_roulette.py
"""
Integration test examples for my‑roulette.

Add concrete scenarios that exercise the full application (e.g. CLI,
HTTP endpoints, database interactions) here.
"""

import subprocess
from pathlib import Path


def _run_cli(args: list[str]) -> subprocess.CompletedProcess:
    """Run the my_roulette module as a script with the given args."""
    cmd = ["uv", "run", "my-roulette"] + args
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=Path(__file__).resolve().parents[2],  # project root
    )


def test_cli_help():
    """Sanity check – the CLI should exit with code 0 and show help."""
    # Arrange
    args = ["--help"]

    # Act
    result = _run_cli(args)

    # Assert
    assert result.returncode == 0, f"CLI exited {result.returncode}\n{result.stderr}"
    # Compare the CLI help output with the expected fixture file.
    expected_help_path = (
        Path(__file__).resolve().parents[2] / "tests" / "fixtures" / "help.txt"
    )
    expected_help = expected_help_path.read_text(encoding="utf-8")
    assert result.stdout == expected_help, (
        f"Help output differs\n--- Expected ---\n{expected_help}\n--- Actual ---\n{result.stdout}"
    )


def _get_stderr_spinner_count(result_stderr):
    """stderrにあるspinnerの文字(|/-\\)を数える"""
    spinner_chars = set("|/-\\")
    return len([ch for ch in result_stderr if ch in spinner_chars])


def test_cli_default():
    """引数なしで呼び出し時、デフォルト値が採用"""
    # Arrange
    args = []

    # Act
    result = _run_cli(args)

    # Assert
    assert result.returncode == 0, f"CLI exited {result.returncode}\n{result.stderr}"

    expected_spins = 1.5 / 0.1
    assert expected_spins == _get_stderr_spinner_count(result.stderr)

    expected_num = int(result.stdout.strip())
    assert 1 <= expected_num <= 6


def test_cli_s_1_e_1():
    # Arrange
    args = ["-s", "1", "-e", "1", "-d", "2.0"]

    # Act
    result = _run_cli(args)

    # Assert
    assert result.returncode == 0, f"CLI exited {result.returncode}\n{result.stderr}"

    expected_spins = 2.0 / 0.1
    assert expected_spins == _get_stderr_spinner_count(result.stderr)

    expected_num = int(result.stdout.strip())
    assert 1 == expected_num


def test_cli_s_10_e_10():
    # Arrange
    args = ["-s", "10", "-e", "10", "-d", "0"]

    # Act
    result = _run_cli(args)

    # Assert
    assert result.returncode == 0, f"CLI exited {result.returncode}\n{result.stderr}"

    assert 0 == _get_stderr_spinner_count(result.stderr)

    expected_num = int(result.stdout.strip())
    assert 10 == expected_num


def test_cli_s_6_e_1():
    # Arrange
    args = ["-s", "6", "-e", "1"]

    # Act
    result = _run_cli(args)

    # Assert
    assert result.returncode == 0, f"CLI exited {result.returncode}\n{result.stderr}"
    expected_num = int(result.stdout.strip())
    assert 1 <= expected_num <= 6
