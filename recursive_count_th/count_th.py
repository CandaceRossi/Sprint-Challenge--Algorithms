'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
from collections import Counter

th = "th"


def count_th(word):
    return word.count('th')
    if word[0].lower() in th:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
