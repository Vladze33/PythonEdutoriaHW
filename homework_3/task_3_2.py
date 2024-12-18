import re
from collections import Counter


def erase_punctuation(string):
    return re.sub(r'\s*([^\w\s])+\s*', ' ', string).strip()


def words_count(string, apply_format=True):
    return Counter(erase_punctuation(string).title().split()) if apply_format \
        else Counter(string.title().split())


input_string = "Test: words, punctuation... Hello dear dear world!"
# input_string = input("Please enter a sentence: ")

formatted_string = erase_punctuation(input_string)
words_stats = words_count(formatted_string, apply_format=False)
print('Unique words count:', len(words_stats))
