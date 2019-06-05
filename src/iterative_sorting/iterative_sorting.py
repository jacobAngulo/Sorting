# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# def selection_sort(arr):

#     for i in arr:
#         for j in arr:
#             if arr[i] < arr[j]:
#                 temp = arr[j]
#                 arr[i] = arr[j]
#                 arr[i] = temp

#     return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    was_sorted = False

    # for i in range(len(arr)):
    #     if i is not 0 and arr[i] < arr[i - 1]:
    #         temp = arr[i]
    #         arr[i] = arr[i-1]
    #         arr[i-1] = temp
    #         was_sorted = True
    #     if was_sorted == True:
    #         i = 0

    i = 0
    while i < len(arr):
        was_sorted = False
        if i is not 0 and arr[i] < arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            was_sorted = True

        if was_sorted == True:
            bubble_sort(arr)
            if was_sorted == True:
                i = 0
        i += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
