# # Time complexity - O(n)
# # Space complexity - O(1)
def firstDuplicateValue(array):
    for idx in range(0, len(array)):
        value = abs(array[idx])
        if array[value - 1] < 0:
            return value
        array[value-1] *= -1
    return -1
