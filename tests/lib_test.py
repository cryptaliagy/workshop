import pytest

import workshop.lib as lib


@pytest.mark.parametrize('subtotal,percentage,expected', [
    (29.25, 10, 2.93),
    (23.85, 11, 2.62),
    (23.28, 15, 3.49)
])
def test_calculate_percent(
    subtotal: float,
    percentage: int,
    expected: float
):
    returned = lib.calculate_percent(subtotal, percentage)

    assert returned == expected


@pytest.mark.parametrize('items,expected', [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55)
])
def test_calculate_subtotal(items, expected):
    actual = lib.calculate_subtotal(*items)

    assert actual == expected
