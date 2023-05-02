def merge_sort(array):
    
    n = len(array)
    if n == 1:
        return array
    mid = n // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result += left_half[i:]
    result += right_half[j:]
    return result

array = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(array))  # Output: [3, 9, 10, 27, 38, 43, 82]
