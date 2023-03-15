#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    scores = list(a_dictionary.values())
    scores.sort()
    best = scores[-1]
    for key in a_dictionary:
        if a_dictionary[key] == best:
            return key
