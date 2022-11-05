DOWN = 0
RIGHT_DIAG = 1
RIGHT = 2
DOWN_DIAG = 3


# Time complexity - O(n)
# Space complexity - O(n)
def zigzagTraverse(array):
    if len(array) == 1:
        return array[0][:]
    current_step = DOWN
    i = 0
    j = 0
    traversed_array = [array[0][0]]
    while i != len(array) - 1 or j != len(array[0]) - 1:
        if current_step == DOWN:
            current_step, i, j = traverse_down(i, j, array, traversed_array)
        elif current_step == RIGHT_DIAG:
            current_step, i, j = traverse_right_diag(i, j, array, traversed_array)
        elif current_step == RIGHT:
            current_step, i, j = traverse_right(i, j, array, traversed_array)
        else:
            current_step, i, j = traverse_down_diag(i, j, array, traversed_array)
    return traversed_array


def traverse_down(i, j, array, traversed_array):
    i += 1
    traversed_array.append(array[i][j])
    if j == len(array[0]) - 1:
        return DOWN_DIAG, i, j
    return RIGHT_DIAG, i, j


def traverse_right_diag(i, j, array, traversed_array):
    steps = min(i, len(array[0])-j-1)
    for _ in range(steps):
        i -= 1
        j += 1
        traversed_array.append(array[i][j])
    if j == len(array[0]) - 1:
        return DOWN, i, j
    return RIGHT, i, j


def traverse_right(i, j, array, traversed_array):
    j += 1
    traversed_array.append(array[i][j])
    if i == len(array) - 1:
        return RIGHT_DIAG, i, j
    return DOWN_DIAG, i, j


def traverse_down_diag(i, j, array, traversed_array):
    steps = min(len(array)-i-1, j)
    for _ in range(steps):
        i += 1
        j -= 1
        traversed_array.append(array[i][j])
    if i == len(array) - 1:
        return RIGHT, i, j
    return DOWN, i, j