#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for x, s in a_dictionary.items():
        if s > maxval:
            maxval = s
            maxkey = x
    return maxkey
