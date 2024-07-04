#!/usr/bin/env python3

"""
Type checking
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list that is the result of multiplying the elements of a
    tuple by a factor.

    Args:
        lst (Tuple): Tuple of integers.
        factor (int, optional): Factor to multiply the elements of the tuple.
        Defaults to 2.

    Returns:
        List: List of integers.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
