#!/usr/bin/python3
"""LockBox implementation"""
from collections import deque


def canUnlockAll(boxes):
    """Lockboxes"""
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key >= 0 and key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
