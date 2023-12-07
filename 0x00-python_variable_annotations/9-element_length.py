#!/usr/bin/env python3
""" File that contains callable function """


from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annoted function """
    return [(i, len(i)) for i in lst]
