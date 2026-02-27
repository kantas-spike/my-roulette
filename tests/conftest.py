import argparse

from unittest.mock import patch

import pytest


@pytest.fixture
def spy_parse_args():
    with patch("my_roulette.parse_args") as m:
        fake = argparse.Namespace(spin_duration=5, start=1, end=6)
        m.return_value = fake
        yield m


@pytest.fixture
def spy_get_spin_count():
    with patch("my_roulette.get_spin_count", return_value=2) as m:
        yield m


@pytest.fixture
def spy_show_spinner():
    with patch("my_roulette.show_spinner") as m:
        yield m


@pytest.fixture
def spy_pick_number():
    with patch("my_roulette.pick_number", return_value=3) as m:
        yield m


@pytest.fixture
def spy_print_selected():
    with patch("my_roulette.print_selected") as m:
        yield m


@pytest.fixture
def spy_print_with_spinner():
    with patch("my_roulette.print_with_spinner") as m:
        yield m


@pytest.fixture
def spy_sleep():
    with patch("my_roulette.sleep") as m:
        yield m


@pytest.fixture
def spy_all_main_deps(
    spy_parse_args,
    spy_get_spin_count,
    spy_show_spinner,
    spy_pick_number,
    spy_print_selected,
):
    """
    main関数で呼びだす以下の関数のモックを作成し返却する
    - parse_args
    - get_spin_count
    - show_spinner
    - pick_number
    - print_selected
    """

    return {
        "parse_args": spy_parse_args,
        "get_spin_count": spy_get_spin_count,
        "show_spinner": spy_show_spinner,
        "pick_number": spy_pick_number,
        "print_selected": spy_print_selected,
    }
