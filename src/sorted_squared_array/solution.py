# Time complexity - O(n)
# Space complexity - O(n)
def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    idx = right
    result_array = [None] * len(array)
    while left <= right:
        if abs(array[left]) > abs(array[right]):
            result_array[idx] = array[left] ** 2
            left += 1
        else:
            result_array[idx] = array[right] ** 2
            right -= 1
        idx -= 1
    return result_array