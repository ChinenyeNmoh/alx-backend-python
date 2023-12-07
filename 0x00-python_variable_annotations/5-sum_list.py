#!/usr/bin/env python3
""" File that contains an add function """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sums up float numbers """
    Total: float = 0.0
    for i in input_list:
        Total += i
    return Total
