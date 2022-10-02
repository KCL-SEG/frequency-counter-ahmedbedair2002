"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        frequencies[str(x)] = frequencies.get(str(x),0) + 1
    return frequencies