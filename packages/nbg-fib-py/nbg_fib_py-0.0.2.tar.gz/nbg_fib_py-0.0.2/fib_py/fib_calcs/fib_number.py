from typing import Optional


def recurring_fibonacci_number(number: int) -> int:
    if number < 0:
        raise ValueError("The number must be equal or above zero")
    elif number <= 1:
        return number
    else:
        return recurring_fibonacci_number(number - 1) + recurring_fibonacci_number(
            number - 2
        )
