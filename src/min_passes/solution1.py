# Time complexity - O(n*m)
# Space complexity - O(n*m)
def minimumPassesOfMatrix(matrix):
	positive_indexes = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] > 0]
	passes = 0
	while positive_indexes:
		new_positive = []
		for element in positive_indexes:
			for child in childs_around(element, matrix):
				i, j = child
				if matrix[i][j] < 0:
					matrix[i][j] *= -1
					new_positive.append((i, j))
		if len(new_positive) > 0:
			passes += 1
		positive_indexes = new_positive
	all_positive = all(matrix[i][j] >= 0 for i in range(len(matrix)) for j in range(len(matrix[0])))
	if all_positive:
		return passes
	return -1

def childs_around(point, matrix):
	i, j = point
	if j > 0:
		yield (i, j-1)
	if j < len(matrix[0]) - 1:
		yield (i, j+1)
	if i > 0:
		yield (i-1, j)
	if i < len(matrix) - 1:
		yield (i+1, j)
