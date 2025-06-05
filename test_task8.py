from hypothesis import given, settings, HealthCheck, Verbosity
from hypothesis.strategies import text


def reverse_words(s):
    """
    Функция разворачивает каждое слово в строке, 
    сохраняя порядок слов.
    Примеры:
    >>> reverse_words("Hello world")
    'olleH dlrow'
    >>> reverse_words("Python is fun")
    'nohtyP si nuf'
    >>> reverse_words("Пример слова")
    'ремирП аволс'
    >>> reverse_words("123 456 789")
    '321 654 987'
    >>> reverse_words("a b c d e")
    'a b c d e'
    """
    words = s.split()
    reversed_words = [word[::-1] for word in words] 
    return ' '.join(reversed_words)

@settings(
    max_examples=200,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow],
    verbosity=Verbosity.verbose
)
@given(text())
def test_strip_not_longer_than_original(s):
    stripped = s.strip()
    assert len(stripped) <= len(s), f"Длина '{stripped}' ({len(stripped)}) > длины '{s}' ({len(s)})"
