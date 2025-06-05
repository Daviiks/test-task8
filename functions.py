def add(a, b):
    """Складывает два числа."""
    return a + b

def subtract(a, b):
    """Вычитает b из a."""
    return a - b

def multiply(a, b):
    """Умножает a на b."""
    return a * b

def divide(a, b):
    """Делит a на b. При b=0 возвращает None."""
    return a / b if b != 0 else None

def is_even(n):
    """Проверяет, чётное ли число."""
    return n % 2 == 0
