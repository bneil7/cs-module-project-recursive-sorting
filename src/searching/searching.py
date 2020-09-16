# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # start = left
    # end = right
    # sys.setrecursionlimit(999)

    # start = 0
    # end = len(arr) - 1

    if end >= start:
        mid = (end + start) // 2
        # if the element is present ad the middle itself
        if arr[mid] == target:
            return mid
        # if the element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > target:
            # search to the left (start) side
            return binary_search(arr, target, start, mid - 1)
        else:
            # move to right (end) side
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
