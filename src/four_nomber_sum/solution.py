from collections import defaultdict


# Time complexity - O(n^2), worst O(n^3)
# Space complexity - O(n^2),
def fourNumberSum(array, targetSum):
	quadruplets = defaultdict(lambda: [])
	sums = []
	for i in range(1, len(array)-1):
		for j in range(i+1, len(array)):
			current_sum = array[i] + array[j]
			diff = targetSum - current_sum
			for pair in quadruplets[diff]:
				sums.append([*pair, array[i], array[j]])
		for k in range(0, i):
			quadruplets[array[k] + array[i]].append([array[k], array[i]])
	return sums
