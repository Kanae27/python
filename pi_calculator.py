#!/usr/bin/env python3
"""
Pi Calculator

This script calculates the value of Pi to a specified number of decimal places
using the Machin formula with arbitrary precision arithmetic using the decimal module.
"""

import argparse
from decimal import Decimal, getcontext


def arctan(x: Decimal, precision: int) -> Decimal:
    """
    Compute arctan(x) using Taylor series expansion.

    Args:
        x: The value to compute arctan for
        precision: Number of terms to use in the series

    Returns:
        Decimal: arctan(x)
    """
    result = Decimal(0)
    term = x
    denom = Decimal(1)
    sign = 1
    for _ in range(precision):
        result += sign * (term / denom)
        sign = -sign
        term *= x * x
        denom += 2
    return result


def get_pi(n: int) -> str:
    """
    Calculate Pi to n decimal places using Machin formula.

    Args:
        n (int): Number of decimal places

    Returns:
        str: Pi as a string with n decimal places
    """
    if n < 0:
        raise ValueError("Number of decimal places must be non-negative")
    if n == 0:
        return "3"

    # Set precision higher than needed
    getcontext().prec = n + 10

    # Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    # So pi = 16*arctan(1/5) - 4*arctan(1/239)

    # Number of terms needed increases with n
    terms = n * 2 + 100  # Rough estimate

    pi = 16 * arctan(Decimal(1) / 5, terms) - 4 * arctan(Decimal(1) / 239, terms)

    # Convert to string and truncate to n decimal places
    pi_str = f"{pi:.{n}f}"
    return pi_str


def main():
    parser = argparse.ArgumentParser(
        description="Calculate Pi to n decimal places",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pi_calculator.py 10    # Pi to 10 decimal places
  python pi_calculator.py 100   # Pi to 100 decimal places
        """
    )
    parser.add_argument(
        "n",
        type=int,
        help="Number of decimal places (must be >= 0)"
    )

    args = parser.parse_args()

    try:
        result = get_pi(args.n)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())