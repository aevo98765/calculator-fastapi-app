def add(x: float, y: float) -> float:
    """
    Adds two floats.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Subtracts one float from another.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The difference of the two numbers.
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Multiplies two floats.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return x * y


def divide(x: float, y: float) -> float | str:
    """
    Divides one float by another. If the divisor is zero, returns an error message instead.

    Args:
        x (float): The dividend.
        y (float): The divisor.

    Returns:
        float | str: Either the result of the division or a division-by-zero error message.
    """
    if y == 0 or x == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y
