#!/usr/bin/python3
def multiple_returns(sentence):
    c1 = None if len(sentence) == 0 else sentence[0]
    return(len(sentence), c1)
