def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#O(n)
# Sample Test Cases
arrayA = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(arrayA, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(arrayA, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(arrayA, target)}")  # Output: -1

def bubble_sort(arr):
    for i in range(len(arr)):
        for ii in range(0, len(arr)-i-1):
            if arr[ii] > arr[ii+1]:
                arr[ii], arr[ii+1] = arr[ii+1], arr[ii]
    return arr
#O(n^2)
# Sample Test Cases
arrayB = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(arrayB)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

arrayC = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(arrayC)}")  # Output: [1, 2, 4, 5, 8]