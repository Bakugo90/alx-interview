#!/usr/bin/python3


"""Sys module
"""

import random
import sys
from time import sleep
import datetime


def compute_metric(dict_sc, total_file_size):
    """
    Method to compute metric and print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file including the sum of previous
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                compute_metric(dict_sc, total_file_size)
                counter = 0

finally:
    compute_metric(dict_sc, total_file_size)
