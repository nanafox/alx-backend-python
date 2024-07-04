#!/usr/bin/env python3

"""
This module contains a type-annotated function safely_get_value that takes a
dictionary and a key as arguments and returns the value of the key in the
dictionary if it exists, otherwise None.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Return the value of the key in the dictionary if it exists, otherwise None.

    Args:
        - dct: Mapping
        - key: Any
        - default: Union[T, None] = None

    Returns:
        Union[Any, T]: the value of the key in the dictionary if it exists,
        otherwise None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
