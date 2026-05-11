"""
Q5. Text Analyzer
Count words, vowels, special characters, find the most frequent word, and replace inappropriate words.
"""

import re
from collections import Counter

BAD_WORDS = ["badword", "stupid", "ugly"]
VOWELS = set("aeiouAEIOU")


def analyze_text(text):
    words = re.findall(r"\b\w+\b", text)
    word_count = len(words)
    vowels = sum(1 for ch in text if ch in VOWELS)
    special_chars = sum(1 for ch in text if not ch.isalnum() and not ch.isspace())
    word_frequency = Counter(word.lower() for word in words)
    most_common = word_frequency.most_common(1)
    most_frequent_word = most_common[0][0] if most_common else None

    return {
        "word_count": word_count,
        "vowel_count": vowels,
        "special_character_count": special_chars,
        "most_frequent_word": most_frequent_word,
        "word_frequency": word_frequency,
    }


def replace_inappropriate_words(text):
    censored = text
    for bad in BAD_WORDS:
        censored = re.sub(rf"\b{bad}\b", "***", censored, flags=re.IGNORECASE)
    return censored


if __name__ == "__main__":
    sample = "Hello world! This is a sample text with a badword and another BadWord."
    result = analyze_text(sample)
    print("Text Analyzer Results")
    print("Words:", result["word_count"])
    print("Vowels:", result["vowel_count"])
    print("Special characters:", result["special_character_count"])
    print("Most frequent word:", result["most_frequent_word"])
    print("Censored text:", replace_inappropriate_words(sample))
