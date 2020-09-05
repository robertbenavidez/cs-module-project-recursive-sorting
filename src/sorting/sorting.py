# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        else:
            if len(arrA) == 0:
                merged_arr[i] = arrB.pop(0)
            else:
                merged_arr[i] = arrA.pop(0)

    return merged_arr


print(merge([5, 2, 6, 9, 7], [3, 4, 1, 8]))


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    arr = merge(left, right)

    return arr


arr1 = [5, 2, 6, 9, 7]
arr2 = [3, 4, 1, 8]
print(merge_sort(merge(arr1, arr2)))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
