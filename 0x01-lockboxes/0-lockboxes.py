#!/usr/bin/python3


"""
    Lockboxes
"""


def canUnlockAll(boxes):
    """
    This function is a method that determines if all the boxes can be opened
    """

    visited = []
    visited.insert(0, boxes[0])

    for boxe in range(len(boxes)):
        if boxes[boxe] == []:
            pass
        for key in range(len(boxes[boxe])):
            idx = boxes[boxe][key]
            if idx != boxe and boxes[idx] not in visited:
                visited.append(boxes[idx])

    return len(visited) == len(boxes)
