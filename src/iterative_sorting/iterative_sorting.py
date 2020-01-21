def insertion_sort( arr ):
    # Separate the first element from the rest of the array.
    # Think about it as a sorted list of one element.
    # For all other indices, beginning with [1]:
    for i in range(1, len(arr)):
        # Copy the item at that index into a temp variable
        temp = arr[i]
        # Iterate to the left until you find the correct index in the 
        # "sorted" part of the array at which this element should be inserted
        j = i
        while temp < arr[j - 1] and j > 0:
            # - Shift items over to the right as you iterate
            arr[j] = arr[j - 1]
            j = j - 1
        # When the correct index is found, copy temp into this position
        arr[j] = temp

    return arr


# test for insertion_sort()
import random
arr = [i for i in range(10)]
random.shuffle(arr)
print(f'unordered: {arr}')
insertion_sort(arr)
print(f'ordered: {arr}')


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


def bubble_sort( arr ):
    # create k for decrementing the length of the inner loop
    k = 0
    for _ in range(0, len(arr) - (1)):
        swapped = False
        # Loop through your array
        for i in range(0, len(arr) - (1 + k)):
            # Compare each element to its neighbor
            # If elements in wrong position (relative to each other, swap them)
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
                swapped = True
        k = k + 1
        # If no swaps performed, stop.
        if swapped == False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr