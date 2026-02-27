import pytest

from my_roulette import pick_number


class TestPickNumber:
    """pick_number関数のテスト"""

    @pytest.mark.parametrize("exec_count", range(10))
    def test_returns_integer_within_range(self, exec_count):
        """開始番号と終了番号の範囲内で整数が返されること"""

        # Arrange
        start_num = 1
        end_num = 6

        # Act
        result = pick_number(start_num, end_num)

        # Assert
        assert isinstance(result, int)
        assert start_num <= result <= end_num, f"{exec_count}回目の結果"

    def test_returns_start_when_range_is_zero(self):
        """開始番号と終了番号が同じ場合、その値が返されること"""

        # Arrange
        start_num = 5
        end_num = 5

        # Act
        result = pick_number(start_num, end_num)

        # Assert
        assert result == 5

    @pytest.mark.parametrize("exec_count", range(10))
    def test_handles_negative_range(self, exec_count):
        """負の範囲でも動作すること"""

        # Arrange
        start_num = -3
        end_num = 3

        # Act
        result = pick_number(start_num, end_num)

        # Assert
        assert isinstance(result, int)
        assert start_num <= result <= end_num, f"{exec_count}回目の結果"
