# Time complexity O(N)
# Space complexity O(d), d - depth
def validateBst(tree):
	return validateHelper(tree, float('-inf'), float('inf'))

def validateHelper(node, minP, maxP):
	if node is None:
		return True
	if node.value < minP or node.value >= maxP:
		return False
	return validateHelper(node.left, minP, node.value) and validateHelper(node.right, node.value, maxP)
