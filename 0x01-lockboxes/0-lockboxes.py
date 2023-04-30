#!/usr/bin/python3

"""
    Lockboxes
"""


def canUnlockAll(boxes):
    """
    This function is a method that determines if all the boxes can be opened
    """
    visited_boxes = set([0])
    unlocked_boxes = [0]

    while unlocked_boxes:
        # idx for the current boxe

        idx = unlocked_boxes.pop(0)
        # retrieve the current box and check all the key

        for key in boxes[idx]:
            if key not in visited_boxes and key < len(boxes):
                visited_boxes.add(key)
                unlocked_boxes.append(key)

    return len(visited_boxes) == len(boxes)
