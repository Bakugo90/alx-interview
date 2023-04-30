#!/usr/bin/python3


"""
    Lockboxes
"""


def canUnlockAll(boxes):
    """
    This function is a method that determines if all the boxes can be opened
    """

    visited = [False] * len(boxes)
    visited[0] = True

    for boxe in range(len(boxes)):
        if visited[boxe]:
            for key in boxes[boxe]:
                if key != boxe and not visited[key]:
                    visited[key] = True

    return all(visited)
