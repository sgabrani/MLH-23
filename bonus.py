#!/usr/bin/env python

import sys

def find_word(letters):
    with open("/usr/share/dict/words", "r") as file:
        for word in file:
            word = word.strip()
            if len(word) == 5 and all(l == "_" or l == word[i] for i, l in enumerate(letters)):
                print(word)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./find_word.py <5-letter string with '_' for unknown letters>")
        sys.exit(1)

    input_letters = sys.argv[1]
    find_word(input_letters)
