"""
General text processing helper functions.
"""

import re
from typing import List

WORD_ENDINGS: List[str] = ["ing", "er", "s", "ed"]

def get_word_list_for_word(word: str) -> List[str]:
    """
    Given a word this generates a list of words with common endings
    and with the ending stripped if the word originally had one.

    Examples:
        "testing" -> ["test", "testing", "tester", "tests", "tested"],
        "work" -> ["work", "working", "worked", "works"]
    """

    word_list: List[str] = [word]

    # Incase the given word already has a common ending
    # we will attempt to remove it first
    for ending in WORD_ENDINGS:
        if word.endswith(ending):
            word = word[:-len(ending)]

    # Word list generation
    for ending in WORD_ENDINGS:
        word_list += [word + ending]

    return word_list

def get_alphanumeric_with_spaces(input_string: str) -> str:
    """
    Given a string this returns the string with all non-alpanumeric characters
    except spaces removed.

    Examples:
        "Hi, I'm Bartek" -> "Hi Im Bartek"
    """
    alphanumeric = re.sub(r'[^A-Za-z0-9 ]+', '', input_string)
    return alphanumeric
