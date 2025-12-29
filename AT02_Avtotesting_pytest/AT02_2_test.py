import pytest
from AT02_2_code import is_polindrom, sort_list
# Проверки для полиндрома
def test_is_polindrom_true():
    assert is_polindrom('madam') == True

def test_is_polindrom_fals():
    assert is_polindrom('hello') == False

@pytest.mark.parametrize('test_input,expected', [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True)
])

def test_is_polindrom(test_input, expected):
    assert is_polindrom(test_input) == expected

# Проверка сортировки
def test_sort1():
    assert sort_list([6, 5, 8, 1, 2]) == [1, 2, 5, 6, 8]

def test_sort2():
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]


