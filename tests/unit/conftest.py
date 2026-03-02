from unittest.mock import patch

import pytest


@pytest.fixture
def spy_pick_number():
    with patch("my_roulette.pick_number", return_value=3) as spy:
        yield spy


@pytest.fixture
def spy_print_with_spinner():
    with patch("my_roulette.print_with_spinner") as spy:
        yield spy


@pytest.fixture
def spy_time_sleep():
    with patch("my_roulette.sleep") as spy:
        yield spy
