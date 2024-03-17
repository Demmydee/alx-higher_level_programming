#!/usr/bin/python3
def multiple_returns(sentence):
    c1 = sentence[0]
    if len(sentence) == 0:
        c1 = None
    return(len(sentence), c1)
