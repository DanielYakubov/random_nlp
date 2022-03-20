"""
script for checking the frequency of letters in the words corpus versus letters in the Brown corpus
as a representation of letters in the dictionary versus which are actually used. Would be better with larger
and newer data than brown but this is a proof of concept and for fun.
"""

import matplotlib.pyplot as plt
import numpy as np
import string

from collections import Counter, defaultdict
from nltk.corpus import words, brown
from typing import List


def char_counter(word_list: List) -> Counter():
    c = Counter()
    for word in word_list:
        for letter in word.lower():
            c[letter] += 1
    return c


def compare_frequencies(c1: Counter(), c2: Counter()) -> defaultdict():
    """returns a dictionary where the key is a common key of both dictionaries
    and the value is a list of frequencies, which is computed by dividing the count
    by the total of the counts in the counter object."""
    d = defaultdict(list)
    for c in [c1, c2]:
        total_letters = sum(c.values())
        for letter, count in c.items():
            if letter in string.ascii_lowercase:
                freq = round(count / total_letters, 30) * 100
                d[letter].append(freq)
    return d


if __name__ == "__main__":
    wrds = words.words()
    brwn = (
        brown.words()
    )  # don't want to remove stop words as we are looking a letter frequencies.
    c_words = char_counter(wrds)
    c_brown = char_counter(brwn)
    d = compare_frequencies(c_words, c_brown)

    for x, v in d.items():
        print(x, ":", v)

    # plotting
    width = 0.35
    fig = plt.subplots(figsize=(12, 8))
    letters, values_list = list(d.keys()), list(d.values())
    wrds_values = [v[0] for v in values_list]
    brwn_values = [v[1] for v in values_list]
    bar1 = np.arange(len(wrds_values))
    bar2 = [x + width for x in bar1]

    plt.bar(
        bar1,
        wrds_values,
        color="g",
        width=width,
        edgecolor="black",
        label="Words Corpus",
    )
    plt.bar(
        bar2,
        brwn_values,
        color="b",
        width=width,
        edgecolor="black",
        label="Brown Corpus",
    )
    plt.xlabel("Letter", fontweight="bold", fontsize=12)
    plt.ylabel("Frequency as a %", fontweight="bold", fontsize=12)
    plt.xticks([r + width for r in range(len(wrds_values))], letters)
    plt.legend()
    plt.show()
