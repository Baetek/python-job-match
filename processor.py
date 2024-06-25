import re
from typing import List

WORD_ENDINGS: List[str] = ["ing", "er", "s", "ed"]

def get_word_list_for_word(word: str) -> List[str]:

    word_list: List[str] = [word]

    for ending in WORD_ENDINGS:
        if word.endswith(ending):
            word_list += [word[:-len(ending)]]
        else:
            word_list += [word + ending]

    return word_list

def get_alphanumeric_with_spaces(input_string: str) -> str:
    alphanumeric = re.sub(r'[^A-Za-z0-9 ]+', '', input_string)
    return alphanumeric
