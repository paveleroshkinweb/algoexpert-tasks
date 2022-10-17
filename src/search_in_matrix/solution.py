# Time complexity - O(n+m)
# Space complexity - O(1)
def searchInSortedMatrix(matrix, target):
    i = 0
    j = len(matrix[0])- 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]
