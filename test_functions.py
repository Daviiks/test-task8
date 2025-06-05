from nose2.tools import params
from functions import add, subtract, multiply, divide, is_even

# Тест для сложения
@params(
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
    (3.5, 2.5, 6.0),
)
def test_add(a, b, expected):
    assert add(a, b) == expected

# Тест для вычитания
@params(
    (5, 3, 2),
    (10, 15, -5),
    (0, 0, 0),
    (7.5, 2.5, 5.0),
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

# Тест для умножения
@params(
    (2, 3, 6),
    (-1, 5, -5),
    (0, 100, 0),
    (1.5, 4, 6.0),
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

# Тест для деления
@params(
    (6, 3, 2.0),
    (10, 2, 5.0),
    (5, 0, None),  # Деление на 0
    (1, 2, 0.5),
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected

# Тест для проверки чётности
@params(
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-7, False),
)
def test_is_even(n, expected):
    assert is_even(n) == expected
