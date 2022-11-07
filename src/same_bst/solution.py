# Time complexity - O(n**2)
# Space complexity - O(d) - depth
def sameBsts(arrayOne, arrayTwo):

    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0:
        return True

    return sameBstsHelper(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def sameBstsHelper(arrayOne, arrayTwo, idx1, idx2, minValue, maxValue):
    if idx1 == idx2 == -1:
        return True
    if idx1 == -1 or idx2 == -1:
        return False
    if arrayOne[idx1] != arrayTwo[idx2]:
        return False

    left1 = find_left(arrayOne, idx1, minValue)
    left2 = find_left(arrayTwo, idx2, minValue)
    right1 = find_right(arrayOne, idx1, maxValue)
    right2 = find_right(arrayTwo, idx2, maxValue)

    return sameBstsHelper(arrayOne, arrayTwo, left1, left2, minValue, arrayOne[idx1]) and sameBstsHelper(arrayOne, arrayTwo, right1, right2, arrayOne[idx1], maxValue)


def find_left(array, idx, minValue):
    for i in range(idx+1, len(array)):
        if array[i] < array[idx] and array[i] >= minValue:
            return i
    return -1


def find_right(array, idx, maxValue):
    for i in range(idx+1, len(array)):
        if array[i] >= array[idx] and array[i] < maxValue:
            return i
    return -1