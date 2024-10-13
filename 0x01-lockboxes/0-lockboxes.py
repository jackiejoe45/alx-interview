#!/usr/bin/python3
def canUnlockAll(boxes):
    knownKeys = {0}
    knownKeys = searchBox(knownKeys,0)
    return (len(knownKeys)==len(boxes))

def searchBox(knownKeys,index):
    for key in boxes[index]:
        if key not in knownKeys:
            knownKeys.add(key)
            searchBox(knownKeys,key)
    return knownKeys
