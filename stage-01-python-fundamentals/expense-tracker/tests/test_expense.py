import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from src.services import add_expense


def test_negative_amount_should_fail():
    with pytest.raises(ValueError):
        add_expense(-100, "Food", "Lunch")


def test_zero_amount_should_fail():
    with pytest.raises(ValueError):
        add_expense(0, "Food", "Lunch")


def test_empty_category_should_fail():
    with pytest.raises(ValueError):
        add_expense(100, "", "Lunch")


def test_empty_note_should_fail():
    with pytest.raises(ValueError):
        add_expense(100, "Food", "")