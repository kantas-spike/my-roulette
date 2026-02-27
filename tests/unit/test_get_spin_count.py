from my_roulette import get_spin_count


class TestGetSpinCount:
    """get_spin_count関数のテスト"""

    def test_returns_correct_count_for_1_second(self):
        """1秒のスピン時間は10回のスリープに対応"""

        # Arrange
        duration = 1.0

        # Act
        result = get_spin_count(duration)

        # Assert
        assert result == 10

    def test_ceil_is_applied(self):
        """小数点以下は切り上げられること"""

        # Arrange
        duration = 0.15

        # Act
        result = get_spin_count(duration)

        # Assert
        assert result == 2

    def test_handles_zero_duration(self):
        """0秒の場合は0回が返されること"""

        # Arrange
        duration = 0.0

        # Act
        result = get_spin_count(duration)

        # Assert
        assert result == 0
