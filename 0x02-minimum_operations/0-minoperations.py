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
    counter = 1
    # count the number of operation
    operation = 0

    while counter < n:
        # count copy operation
        if n % counter == 0:
            operation += 1
        # count past operation
        counter *= 2
        operation += 1
    return operation
