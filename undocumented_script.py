"""Refactored and documented version of undocumented_script.py.

This module provides two functions:
- transform_numbers: double even numbers and triple odd numbers.
- process_strings: uppercase long strings and lowercase short strings, then join with spaces.

It also includes a simple main() to demonstrate usage.
"""

from typing import List


def transform_numbers(numbers: List[int]) -> List[int]:
    """Return a new list where even numbers are doubled and odd numbers are tripled.

    Args:
        numbers: A list of integers to transform.

    Returns:
        A list of integers where each even number is multiplied by 2
        and each odd number is multiplied by 3.
    """
    # Double even numbers, triple odd numbers
    return [n * 2 if n % 2 == 0 else n * 3 for n in numbers]


def process_strings(strings: List[str]) -> str:
    """Return a single space-separated string after case-transforming each input.

    Any string with length greater than 5 is converted to uppercase.
    Any string with length 5 or less is converted to lowercase.

    Args:
        strings: A list of strings to process.

    Returns:
        A single string that joins the transformed items with spaces.
    """
    # Uppercase long strings, lowercase short ones, then join with spaces
    return " ".join(s.upper() if len(s) > 5 else s.lower() for s in strings)


def main() -> None:
    """Demonstrate basic usage of the transformation functions."""
    numbers_example = [1, 2, 3, 4, 5, 6, 7]
    fruit_names = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    transformed = transform_numbers(numbers_example)
    processed = process_strings(fruit_names)

    print("Processed Numbers:", transformed)
    print("Processed Strings:", processed)


if __name__ == "__main__":
    main()
