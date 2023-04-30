from collections import deque

def canUnlockAll(boxes):
    """
    This function is a method that determines if all the boxes can be opened
    """
    n = len(boxes)
    visited = set([0])
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key not in visited and key < n:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
