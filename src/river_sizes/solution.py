# Time complexity - O(n*m)
# Space complexity - O(n*m)
def riverSizes(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    rivers = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if visited[i][j]:
                continue
            if matrix[i][j] == 1:
                river_size = bfs(matrix, visited, (i, j))
                rivers.append(river_size)
            visited[i][j] = True
    return rivers

def bfs(matrix, visited, vertex):
    queue = [vertex]
    count = 0
    while queue:
        i, j = queue.pop(0)
        if visited[i][j] or matrix[i][j] == 0:
            continue
        visited[i][j] = True
        count += 1
        if i < len(matrix) - 1:
            queue.append((i+1, j))
        if i > 0:
            queue.append((i-1, j))
        if j < len(matrix[0]) - 1:
            queue.append((i, j+1))
        if j > 0:
            queue.append((i, j-1))
    return count