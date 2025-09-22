from collections import Counter
from typing import List, Tuple

def word_count(text: str) -> int:
    return len(text.split())

def top_n_words(text: str, n: int) -> List[Tuple[str, int]]:
    words = [w.strip().lower() for w in text.split() if w.strip()]
    counts = Counter(words)
    return counts.most_common(n)

def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))