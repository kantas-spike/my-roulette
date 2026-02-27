import sys

from my_roulette import (
    DEFAULT_END_NUM,
    DEFAULT_SPIN_DURATION,
    DEFAULT_START_NUM,
    parse_args,
)


class TestParseArgs:
    """
    parse_argsのテスト
    """

    def test_default_values(self, monkeypatch):
        """CLI引数に何も指定されない場合、デフォルト値が採用されること"""

        # Arrange
        monkeypatch.setattr("sys.argv", ["my-roulette"])

        # Act
        args = parse_args()

        # Assert
        assert args.start == DEFAULT_START_NUM
        assert args.end == DEFAULT_END_NUM
        assert args.spin_duration == DEFAULT_SPIN_DURATION

    def test_set_short_option(self, monkeypatch):
        """CLI引数にショートオプションが指定された場合、指定された値が採用されること"""
        # Arrange
        monkeypatch.setattr(
            "sys.argv", ["my-roulette", "-s", "2", "-e", "3", "-d", "4"]
        )

        # Act
        args = parse_args()

        # Assert
        assert args.start == 2
        assert args.end == 3
        assert args.spin_duration == 4

    def test_set_long_option(self, monkeypatch):
        """CLI引数にロングオプションが指定された場合、指定された値が採用されること"""
        # Arrange
        monkeypatch.setattr(
            "sys.argv",
            ["my-roulette", "--start", "2", "--end", "3", "--spin-duration", "4"],
        )

        # Act
        args = parse_args()

        # Assert
        assert args.start == 2
        assert args.end == 3
        assert args.spin_duration == 4
