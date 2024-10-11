#!/usr/bin/python3
"""
    Lockboxes
"""


def canUnlockAll(boxes):
    """
        A method that determines if all the boxes can be opened.
    """
    keys = set(boxes[0])
    keys.update({box for k in keys for box in boxes[k]})
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
        keys.update({x for x in boxes[i]})
    return True
