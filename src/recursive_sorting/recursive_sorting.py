# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    for i in range(len(merged_arr)):
        if len(arrA) is not 0:
            if len(arrB) is not 0:
                if arrA[0] <= arrB[0]:
                    merged_arr[i] = arrA[0]
                    arrA.pop(0)
                elif arrA[0] >= arrB[0]:
                    merged_arr[i] = arrB[0]
                    arrB.pop(0)
            else:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    global merge
    left_sorted = False
    right_sorted = False
    mid_point = int(len(arr)/2)
    left_side = arr[:mid_point]
    right_side = arr[mid_point:]
    if len(right_side) <= 1:
        right_sorted = True
    if len(left_side) <= 1:
        left_sorted = True
    if left_sorted == True and right_sorted == True:
        return merge(left_side, right_side)
    elif left_sorted == True and right_sorted is not True:
        right_side = merge_sort(right_side)
        return merge(left_side, right_side)
    elif right_sorted == True and left_sorted is not True:
        left_side = merge_sort(left_side)
        return merge(left_side, right_side)
    elif right_sorted == False and left_sorted == False:
        right_side = merge_sort(right_side)
        left_side = merge_sort(left_side)
        return merge(left_side, right_side)

    return merge(left_side, right_side)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
