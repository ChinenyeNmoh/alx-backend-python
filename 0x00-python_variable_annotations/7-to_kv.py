#!/usr/bin/env python3
""" File that contains mixed tuple function """


from typing import List, Union, Tuple

int_float = Union[int, float]


def to_kv(k: str, v: int_float) -> Tuple[str, float]:
    """ returns a tuple """
    return (k, v ** 2)
