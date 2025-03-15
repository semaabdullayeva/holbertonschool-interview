#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and,
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    unlockedBoxes = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key not in unlockedBoxes and key < len(boxes):
            unlockedBoxes.add(key)
            keys.extend(boxes[key])

    return len(unlockedBoxes) == len(boxes)
