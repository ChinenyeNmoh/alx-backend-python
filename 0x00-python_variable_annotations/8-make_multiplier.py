#!/usr/bin/env python3
""" File that contains callable function """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ main function """
    def func(x: float) -> float:
        """ return function """
        return x * multiplier
    return func
