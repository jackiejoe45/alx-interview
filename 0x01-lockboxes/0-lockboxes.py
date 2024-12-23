#!/usr/bin/python3
"""
This module checks boxes to see if they contain keys to unlock all other boxes
"""


def canUnlockAll(boxes):
    """ checks if a box can be unlocked"""
    knownKeys = {0}
    searchBox(boxes, knownKeys, 0)
    return (len(knownKeys) == len(boxes))


def searchBox(boxes, knownKeys, index):
    """ recursively searches boxes for keys"""
    for key in boxes[index]:
        if key < len(boxes) and key not in knownKeys:
            knownKeys.add(key)
            searchBox(boxes, knownKeys, key)
