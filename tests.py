from hw2_debugging import merge_sort

def test1():
    arr = [10, 9, 77, 3, 5, 20, 35]
    output = [3, 5, 9, 10, 20, 35, 77]
    assert merge_sort(arr) == output

def test2():
    arr = [100, 50, 89, 23, 1, 7, 255]
    output = [1, 7, 23, 50, 89, 100, 255]
    assert merge_sort(arr) == output

def test3():
    arr = [15, 29, 2, 66, 34, 99, 40]
    output = [2, 15, 29, 34, 40, 66, 99]
    assert merge_sort(arr) == output