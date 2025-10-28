import logging


module_logger = logging.getLogger(__name__)


def example_add(x: float, y: float) -> float:
    """Add the Ratio `y/x` to the given value of `x`

    This is just a random example to show docstrings, a function definition, and the use
    of typehints for the design of a modern Python function.

    Args:
        x (float): Base for Addition and Scale Reference for `y`
        y (float): Value to be scaled by `x` before  adding to `x`

    Returns:
        float: Sum of `x` plus the ratio of `y` over `x`

    Raises:
        DivideByZeroError: If `x` is `0`.
    """
    scaled_y: float = (y / x)
    z: float = x + scaled_y

    module_logger.debug(f"🧮 (y / x) Value: {scaled_y}")

    return z
