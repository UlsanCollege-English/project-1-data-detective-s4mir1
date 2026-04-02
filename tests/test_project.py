import pytest
from src.project import (
    load_text,
    normalize_text,
    tokenize,
    count_words,
    top_n_words,
    extra_insight,
)


def test_normalize_text():
    text = "Hello, World!"
    assert normalize_text(text) == "hello world"


def test_tokenize():
    text = "hello world"
    assert tokenize(text) == ["hello", "world"]


def test_tokenize_empty():
    assert tokenize("") == []


def test_count_words():
    words = ["apple", "banana", "apple"]
    result = count_words(words)
    assert result == {"apple": 2, "banana": 1}


def test_top_n_words():
    counts = {"apple": 2, "banana": 3, "cherry": 1}
    result = top_n_words(counts, 2)
    assert result == [("banana", 3), ("apple", 2)]


def test_top_n_words_zero():
    counts = {"apple": 2}
    assert top_n_words(counts, 0) == []


def test_extra_insight_average_length():
    words = ["hi", "hello"]
    counts = count_words(words)
    result = extra_insight(words, counts)
    assert result == 3.5  # (2 + 5) / 2


def test_extra_insight_empty():
    assert extra_insight([], {}) == 0.0


def test_load_text_file_not_found():
    assert load_text("nonexistent.txt") == ""