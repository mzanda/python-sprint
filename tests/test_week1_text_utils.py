import pytest
from src.week1_text_utils.core import word_count, top_n_words, reverse_words

def test_word_count_basic():
    assert word_count("hello world") == 2
    assert word_count("") == 0

@pytest.mark.parametrize(
    "text,n,expected",
    [
        ("a a a b b c", 2, [("a", 3), ("b", 2)]),
        ("One two two THREE three three", 3, [("three", 3), ("two", 2), ("one", 1)]),
    ],
)
def test_top_n_words(text, n, expected):
    assert top_n_words(text, n) == expected

def test_reverse_words():
    assert reverse_words("hello brave new world") == "world new brave hello"