#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function."""

    def multiplier_function(x: float) -> float:
        """Multiply a float by the stored multiplier."""
        return x * multiplier

    return multiplier_function
