# Time complexity - O(n)
# Space complexity - O(1)
def isMonotonic(array):
    isNotIncreasing = True
    isNotDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNotDecreasing = False
        if array[i] < array[i-1]:
            isNotIncreasing = False
        if not isNotDecreasing and not isNotIncreasing:
            return False
    return True
