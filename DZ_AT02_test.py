import pytest
from DZ_AT02_code import count_vowels

@pytest.mark.parametrize('line, expected', [
    ('fdskjhvyfeedsv', 3),
    ('авылвкрлов вке', 4),
    ('fdskjhr кртн', 0),
    ('ээeyu uy', 7),
    ('FGREUdfiuАОГК ркЦуRTU', 8)
])

def test_1(line, expected):
    assert count_vowels(line) == expected
