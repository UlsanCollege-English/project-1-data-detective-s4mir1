from typing import List, Dict, Tuple
import string


def load_text(path: str) -> str:
    """Load text from a UTF-8 file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def normalize_text(text: str) -> str:
    """
    Normalize text by:
    - converting to lowercase
    - removing punctuation
    """
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))


def tokenize(text: str) -> List[str]:
    """Split normalized text into words."""
    if not text.strip():
        return []
    return text.split()


def count_words(words: List[str]) -> Dict[str, int]:
    """Count frequency of each word."""
    counts: Dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n_words(counts: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """
    Return top N most common words sorted by frequency (desc),
    then alphabetically for ties.
    """
    if n <= 0:
        return []

    sorted_words = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )
    return sorted_words[:n]


def extra_insight(words: List[str], counts: Dict[str, int]) -> float:
    """
    Extra insight: average word length.
    Returns 0.0 if no words.
    """
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# Optional helper for demo (not required but useful)
def analyze_file(path: str, n: int = 5) -> dict:
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "average_word_length": extra_insight(words, counts),
    }