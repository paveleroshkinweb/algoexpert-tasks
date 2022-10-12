# Time complexity - O(n**2)
# Space complexity - O(1)
def firstDuplicateValue(array):
    minimal_duplicate = len(array)
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                minimal_duplicate = min(minimal_duplicate, j)
    if minimal_duplicate == len(array):
        return -1
    return array[minimal_duplicate]
