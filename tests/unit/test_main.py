import argparse
from unittest.mock import call


from my_roulette import (
    main,
)


class TestMain:
    """main関数のテスト"""

    def test_calls_parse_args(self, spy_all_main_deps):
        """parse_argsが呼び出されること"""
        # Act
        main()

        # Assert
        assert 1 == spy_all_main_deps["parse_args"].call_count
        assert [call()] == spy_all_main_deps["parse_args"].mock_calls

    def test_calls_get_spin_count(self, spy_all_main_deps):
        """get_spin_countが呼び出されること"""

        # Act
        main()

        # Assert
        assert 1 == spy_all_main_deps["get_spin_count"].call_count
        assert [call(5)] == spy_all_main_deps["get_spin_count"].mock_calls

    def test_calls_show_spinner(self, spy_all_main_deps):
        """show_spinnerが呼び出されること"""
        # Act
        main()

        # Assert
        assert 1 == spy_all_main_deps["show_spinner"].call_count
        assert [call(1, 6, 2)] == spy_all_main_deps["show_spinner"].mock_calls

    def test_calls_pick_number(self, spy_all_main_deps):
        """pick_numberが呼び出されること"""
        # Act
        main()

        # Assert
        assert 1 == spy_all_main_deps["pick_number"].call_count
        assert [call(1, 6)] == spy_all_main_deps["pick_number"].mock_calls

    def test_calls_print_selected(self, spy_all_main_deps):
        """print_selectedが呼び出されること"""
        # Act
        main()

        # Assert
        assert 1 == spy_all_main_deps["print_selected"].call_count
        assert [call(3)] == spy_all_main_deps["print_selected"].mock_calls

    def test_calls_start_larger_end(self, spy_all_main_deps):
        """startオプションの値 > endオプションの値の場合、startとendを入れ替えて呼び出されること"""
        # Arrange
        spy_all_main_deps["parse_args"].return_value = argparse.Namespace(
            spin_duration=5,
            start=6,
            end=1,
        )
        # Act
        main()

        # Assert
        assert [call(1, 6, 2)] == spy_all_main_deps["show_spinner"].mock_calls
        assert [call(1, 6)] == spy_all_main_deps["pick_number"].mock_calls
