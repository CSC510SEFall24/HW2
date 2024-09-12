"""Module for generating random arrays."""

import random


def random_array(arr):
    """
    Fill the input array with random integers between 1 and 20.

    Args:
        arr (list): The array to be filled with random numbers.

    Returns:
        list: The input array filled with random numbers.
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
