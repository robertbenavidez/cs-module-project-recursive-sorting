# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    return binary_search_helper(arr, target, 0, len(arr) - 1)


def binary_search_helper(arr, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = arr[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binary_search_helper(arr, target, left, middle - 1)
    else:
        return binary_search_helper(arr, target, middle + 1, right)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
