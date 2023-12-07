#!/usr/bin/env python3
"""File that contains safely_get_value function"""


from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None]
) -> Union[Any, T]:
    """ Function that return values, add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
