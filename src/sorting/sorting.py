# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # check whether the value at index[0] of left > value at index[0] of right
    # put the lesser value first
    # merged_arr[0] = arrB[0]

    # keep track of where we are in both arrays
    arrA_index = 0
    arrB_index = 0
    merged_arr_index = 0  # COUNTER

    # check whether both arrays have values
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        # if value at index of arrA > value at indx of arrB
        #   replace value at index of merged_arr with value at index of arrB
        if arrA[arrA_index] >= arrB[arrB_index]:
            merged_arr[merged_arr_index] = arrB[arrB_index]
            # increment counter by 1 to go to the next index
            merged_arr_index += 1
            arrB_index += 1
        else:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index += 1
            arrA_index += 1

    # check if arrA is empty, if it is, dump values of arrB into sorted array
    if arrA_index == len(arrA):
        for item in arrB[arrB_index:]:
            merged_arr[merged_arr_index] = arrB[arrB_index]
            merged_arr_index += 1
            arrB_index += 1

    # check if arrB is empty, if it is, dump values of arrA into sorted array
    elif arrB_index == len(arrB):
        for item in arrA[arrA_index:]:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index += 1
            arrA_index += 1

    return merged_arr


# expects a SORTED ARRAY, so uhhh.. sort your arrays....
print(merge([3, 4], [1, 5]))


# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    if len(arr) > 1:
        # ( // ) divide for integer division, instead of float
        mid = len(arr) // 2
        left_array = arr[:mid]
        left_side = merge_sort(left_array)
        right_array = arr[mid:]
        right_side = merge_sort(right_array)
        return merge(left_side, right_side)
    else:
        return arr


#---------------------------#
# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
