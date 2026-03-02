from unittest.mock import call

import pytest

from my_roulette import SLEEP_SEC, show_spinner


class TestShowSpinner:
    """show_spinner関数のテスト"""

    @pytest.mark.parametrize("spin_count", [5, 0])
    def test_spins_correct_number_of_times(
        self, spin_count, spy_pick_number, spy_print_with_spinner, spy_time_sleep
    ):
        """指定回数だけスピンすること"""

        # Arrange
        start_num = 1
        end_num = 6

        # Act
        show_spinner(start_num, end_num, spin_count)

        # Assert
        assert spy_pick_number.call_count == spin_count
        assert spy_print_with_spinner.call_count == spin_count
        assert spy_time_sleep.call_count == spin_count

    def test_passes_correct_arguments(
        self, spy_pick_number, spy_print_with_spinner, spy_time_sleep
    ):
        # Arrange
        start_num = 1
        end_num = 6
        spin_count = 5

        # Act
        show_spinner(start_num, end_num, spin_count)

        # Assert
        assert 5 == spy_pick_number.call_count
        assert [call(1, 6)] * 5 == spy_pick_number.mock_calls

        assert 5 == spy_print_with_spinner.call_count
        assert [call(3, i) for i in range(5)] == spy_print_with_spinner.mock_calls

        assert 5 == spy_time_sleep.call_count
        assert [call(SLEEP_SEC)] * 5 == spy_time_sleep.mock_calls
