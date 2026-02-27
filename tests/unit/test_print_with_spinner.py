import pytest

from my_roulette import (
    CS_ERASE_LINE,
    CS_HEAD_OF_LINE,
    CS_INVERT_COLORS,
    CS_RESET_COLORS,
    print_with_spinner,
)


class TestPrintWithSpinner:
    """print_with_spinner関数のテスト"""

    def test_writes_to_stderr(self, capsys):
        """標準エラー出力に書き込まれること"""

        # Arrange
        displayed_num = 3
        sleep_count = 0

        # Act
        print_with_spinner(displayed_num, sleep_count)

        # Assert
        captured = capsys.readouterr()
        assert (
            f"{CS_ERASE_LINE}{CS_HEAD_OF_LINE}{CS_INVERT_COLORS}{displayed_num}{CS_RESET_COLORS}"
            in captured.err
        ), "標準エラーにエスケープシーケンスが出力されること"

    @pytest.mark.parametrize(
        "spin_mark,spin_times",
        [
            ("|", 0),
            ("/", 1),
            ("-", 2),
            ("\\", 3),
            ("|", 4),
            ("/", 5),
            ("-", 6),
            ("\\", 7),
        ],
    )
    def test_shows_correct_spinner_letter(self, capsys, spin_mark, spin_times):
        """正しいスピン文字が表示されること"""

        # Arrange
        displayted_num = 1

        # Act
        print_with_spinner(displayted_num, spin_times)

        # Assert
        cap = capsys.readouterr()
        assert spin_mark in cap.err, "スピン回数に対応するスピン文字が表示されること"
