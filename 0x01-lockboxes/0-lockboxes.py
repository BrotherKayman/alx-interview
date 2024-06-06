#!/usr/bin/python3
"""Solves the lock boxes puzzle"""


def find_next_box(checked_boxes):
    """
    Finds the next box to check.

    Args:
        checked_boxes (dict): Dictionary containing boxes that have been opened and checked.

    Returns:
        list: List of keys found in the next box to check, or None if no boxes are left to check.
    """
    for index, box in checked_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): List where each element is a list of keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if len(boxes) == 0 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if len(opened_boxes) == 0:
            opened_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    if opened_boxes.get(key) and opened_boxes.get(key).get('status') == 'checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)


def main():
    """Entry point"""
    pass


if __name__ == '__main__':
    main()
