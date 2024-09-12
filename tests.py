"""
Tests for hw2_debugging
"""
import pytest
from hw2_debugging import merge_sort

def test1():
    """
    Test 1 for Merge Sort
    Returns:
        True if test passes
        False if test fails
    """
    arr = [10, 9, 77, 3, 5, 20, 35]
    merge_sort(arr)

def test2():
    """
    Test 2 for Merge Sort
    Returns:
        True if test passes
        False if test fails
    """
    arr = [100, 50, 89, 23, 1, 7, 255]
    merge_sort(arr)

def test3():
    """
    Test 3 for Merge Sort
    Returns:
        True if test passes
        False if test fails
    """
    arr = [15, 29, 2, 66, 34, 99, 40]
    merge_sort(arr)

if __name__ == "__main__":
    pytest.main()