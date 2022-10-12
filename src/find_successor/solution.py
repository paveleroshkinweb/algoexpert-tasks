# Time complexity - O(d), d - depth
# Space complexity - O(1)
def findSuccessor(tree, node):
	if node.right is not None:
		return findLeft(node.right)
	return findParent(node)

def findLeft(node):
	current = node
	while current.left is not None:
		current = current.left
	return current

def findParent(node):
	if node.parent is None:
		return None
	if node.parent.left is node:
		return node.parent
	if node.parent.parent is not None:
		return node.parent.parent