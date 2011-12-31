def inversion_count(array, count=0):
    """
    Sorts and returns the no of inversions in an array permutation using merge-sort
    """
    if len(array) < 2: return array, count
    mid = len(array) // 2
    left, right = array[:mid], array[mid:]
    return icombine(inversion_count(left, count), inversion_count(right, count))

def icombine(left, right):
    left_array, left_count = left
    right_array, right_count = right
    l, r = 0, 0
    count = left_count + right_count
    result = []
    while l < len(left_array) and r < len(right_array):
        if left_array[l] <= right_array[r]:
            result.append(left_array[l])
            l += 1
        else:
            result.append(right_array[r])
            r += 1
            count += len(left_array) - l
    result += left_array[l:] + right_array[r:]
    return result, count

