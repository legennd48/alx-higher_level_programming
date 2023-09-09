#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        x = len(sentence)
        if x > 0:
            return (x, sentence[0])
        else:
            return (0, 'None')
