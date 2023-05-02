def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    pivot = array[n // 2]
    left_half, right_half = partition(array, pivot)

    return quick_sort(left_half) + quick_sort(right_half)

def partition(array, pivot):
    
    left_half = []
    right_half = []

    for num in array:
        if num < pivot:
            left_half.append(num)
        elif num > pivot:
            right_half.append(num)

    return left_half, right_half

array = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(array))
