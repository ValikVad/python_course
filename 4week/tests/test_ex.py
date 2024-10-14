import time

import pytest


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


@pytest.mark.timeout(0)
def test_add_timeout():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


@pytest.mark.timeout(1)
def test_add_timeout_fail():
    time.sleep(2)
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


@pytest.mark.skip(reason="This test is skipped for demonstration.")
def test_add_skip():
    # ошибка не выпадает
    assert add(2, 3) == 6


# каждый набор параметров опредяется как отдельный тест
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (-1, -1, -2),
    ],
)
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected
