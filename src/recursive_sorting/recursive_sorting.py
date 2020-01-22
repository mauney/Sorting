def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr))
    
def quick_sort_helper(arr, low, high):
    # 1. Pick a pivot and move it until everything
    # on the left is smaller & everything on the right is greater
    if low >= high:
        return
    pivot_index = high - 1
    for i in range(high - 1, low - 1, -1):
        if arr[pivot_index] < arr[i]:
            # do double swap
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            arr[i], arr[pivot_index - 1] = arr[pivot_index - 1], arr[i]
            pivot_index -= 1
    quick_sort_helper(arr, low, pivot_index)
    quick_sort_helper(arr, pivot_index + 1, high)



# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a_index = 0
    b_index = 0
    for i in range(elements):
        # check to see if either array is exhausted
        if a_index >= len(arrA):
            merged_arr = merged_arr[:i] + arrB[b_index:]
            break
        if b_index >= len(arrB):
            merged_arr = merged_arr[:i] + arrA[a_index:]
            break
        # otherwise, insert the next item
        if arrA[a_index] <= arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[i] = arrB[b_index]
            b_index += 1
    
    return merged_arr

def merge_create( arrA, arrB ):
    merged_arr = []
    # TO-DO
    a_index = 0
    b_index = 0
    for _ in range(len( arrA ) + len( arrB )):
        # check to see if either array is exhausted
        if a_index >= len(arrA):
            merged_arr += arrB[b_index:]
            break
        if b_index >= len(arrB):
            merged_arr += arrA[a_index:]
            break
        # otherwise, insert the next item
        if arrA[a_index] <= arrB[b_index]:
            merged_arr.append(arrA[a_index])
            a_index += 1
        else:
            merged_arr.append(arrB[b_index])
            b_index += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <=1:
        return arr

    mid = len(arr) // 2
    lhs = merge_sort(arr[:mid])
    rhs = merge_sort(arr[mid:])

    return merge_create(lhs, rhs)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr



import random
import time
# x = [random.randint(0, 10000000) for _ in range(1000000)]
# y = [random.randint(0, 10000000) for _ in range(1000000)]
# print(f'x pre: {x}')
# print(f'y pre: {y}')
# x.sort()
# y.sort()
# print(f'x post: {x}')
# print(f'y post: {y}')
# print(merge(x, y))

# start_time = time.time()
# merge(x, y)
# end_time = time.time()
# print(f'Time for merge: {end_time - start_time}')

# start_time = time.time()
# merge_create(x, y)
# end_time = time.time()
# print(f'Time for merge_create: {end_time - start_time}')


x = [random.randint(0, 100000) for _ in range(10000)]
start_time = time.time()
y = merge_sort(x)
end_time = time.time()
print(f'Time for merge_sort: {end_time - start_time}')

x = [random.randint(0, 100000) for _ in range(10000)]
start_time = time.time()
y = quick_sort(x)
end_time = time.time()
print(f'Time for quick_sort: {end_time - start_time}')