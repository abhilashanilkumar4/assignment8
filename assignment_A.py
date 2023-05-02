def binary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [1, 3, 5, 7, 9]
x = 5
print(binary_search(arr, x)) 
