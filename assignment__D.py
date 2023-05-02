def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array

array = [55, 16, 23, 2, 10, 72, 9]
print(insertion_sort(array))
