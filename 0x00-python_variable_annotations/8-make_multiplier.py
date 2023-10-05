#!/usr/bin/env python3
"""
using Callable type to multiply a function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates and returns a function that multiplies
    a float by the given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the product of the input and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply a float by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of multiplying value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
