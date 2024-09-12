"""Module for implementing merge sort algorithm."""

import rand


def merge_sort(input_arr):
    """
    Perform merge sort on the input array.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The merged sorted array.
    """
    left_index = 0
    right_index = 0
    # Initialize an empty list instead of a fixed-size array with None values
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Add the remaining elements of both arrays
    merge_arr.extend(right_arr[right_index:])
    merge_arr.extend(left_arr[left_index:])

    return merge_arr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
