"""
SORTING

There are many different ways to sort a list. Some are more efficient than others.

Python provides a couple of ways to sort a list. The most common way is to use the built-in `sort` method on
the list directly. This method sorts the list in place. You can also use the `sorted` function which returns a new
sorted list without modifying the original list.

The purpose of this exercise, however, is to have you write your own sorting algorithm. The algorithm should take a list
and an order parameter. The order parameter can be either "asc" for ascending order or "desc" for descending order.

Here are some good places to look for sorting algorithms:
- Bubble sort
- Selection sort
- Insertion sort
- Merge sort

Google is your friend. Look up these algorithms and try to implement one of them.

You cannot use the built-in `sort` method or the `sorted` function. You must write your own sorting algorithm.

This excercise will introduce the concept of unit tests, and algorithm complexity.

The unit tests can be found in the file 003/test_sort.py

To run the tests simply run `pytest` in the terminal (after having done `pip install -r requirements.txt`)
"""


def manual_sort(list: list, *, order: str) -> int:
    """
    Sorts a list in ascending or descending order based on the given order parameter.

    Args:
        list: The list to be sorted.
        order: The order in which to sort the list. Can be either "asc" for ascending order or "desc" for descending order.

    Returns:
        The sorted list.

    """
    def merge(left: list, right: list) -> list:

        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        
        result = []
        il = 0
        ir = 0
        while len(result) < len(left) + len(right):
            if left[il] <= right[ir]:
                result.append(left[il])
                il += 1
            else:
                result.append(right[ir])
                ir += 1

            if ir == len(right):
                result += left[il:]
                break

            if il == len(left):
                result += right[ir:]
                break

        return result

    def merge_sort(array: list) -> list:
        if len(array) < 2:
            return array
        middle = len(array) // 2 # divide by 2 without a remainder
        result = merge(left=merge_sort(array[:middle]),right=merge_sort(array[middle:]))
        return result

    result = merge_sort(list)
    if order == "desc":
        result.reverse()

    return result