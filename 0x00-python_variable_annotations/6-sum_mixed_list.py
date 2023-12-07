#!/usr/bin/env python3
""" File that contains mixed list function """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums up float and int numbers """
    Total: float = 0.0
    for i in mxd_lst:
        Total += i
    return Total
