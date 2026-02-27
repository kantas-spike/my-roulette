from my_roulette import CS_ERASE_LINE, CS_HEAD_OF_LINE, print_selected


class TestPrintSelected:
    """print_selected関数のテスト"""

    def test_writes_number_and_newline(self, capsys):
        """数値と改行が書き込まれること"""

        # Arrange
        displayed_num = 7

        # Act
        print_selected(displayed_num)

        # Assert
        captured = capsys.readouterr()
        assert f"{CS_ERASE_LINE}{CS_HEAD_OF_LINE}" == captured.err
        assert f"{displayed_num}\n" == captured.out
