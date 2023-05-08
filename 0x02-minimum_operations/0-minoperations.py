#!/usr/bin/python3
"""minOperations

"""


def minOperations(n):
    """a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
    The number for which, we are searching the minimum operation
    """

    # this variable count tne number of 'H' in the file
    h_counter = 1
    # count the number of operation
    ops_counter = 0
    copy = 0

    if not isinstance(n, int):
        return 0

    while h_counter < n:
        # first copy
        if copy == 0:
            copy = h_counter
            h_counter += copy
            ops_counter += 2
        # copy all and past
        elif n - h_counter > 0 and (n - h_counter) % h_counter == 0:
            copy = h_counter
            h_counter += copy
            ops_counter += 2
        # simple past
        elif copy > 0:
            h_counter += copy
            ops_counter += 1
    return ops_counter
