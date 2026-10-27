
import pytest

from tasks.buggy_project.calculator import calculate_total


def test_calculate_total_with_tax():
    assert calculate_total(100, 0.10) == pytest.approx(110)


def test_calculate_total_without_tax():
    assert calculate_total(100, 0.0) == pytest.approx(100)


def test_calculate_total_with_zero_price():
    assert calculate_total(0, 0.10) == pytest.approx(0)
