import pytest
from AT02_avtotest_pytest import check

def test_check():
    assert check(8) == True

def test_check2():
    assert check(7) == False

@pytest.mark.parametrize('numbers, expected', [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False)
])

def test_check3(numbers, expected):
    assert check(numbers) == expected
