#Implementation of Bubble Sort in Python 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:  # no swaps -> already sorted
            break
    return arr

# Example
nums = [5, 3, 8, 4, 2]
print(bubble_sort(nums))  # [2, 3, 4, 5, 8]

