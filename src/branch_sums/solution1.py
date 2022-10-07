# Time complexity - O(N)
# Space complexity - average O(logN), where h is the height of a tree. worst O(N)
def branchSums(root):
    if not root:
        return []

    stack = [(root, 0)]
    branch_sums = []
    while stack:
        node, current_sum = stack.pop()
        
        if node.left is None and node.right is None:
            branch_sums.append(current_sum + node.value)

        if node.right is not None:
            stack.append((node.right, current_sum + node.value))

        if node.left is not None:
            stack.append((node.left, current_sum + node.value))

    return branch_sums
