def branchSums(root):
    branch_sums = []
    branchSumsHelper(root, branch_sums, 0)
    return branch_sums
    
# Time complexity - O(N)
# Space complexity - average O(logN), where h is the height of a tree. worst O(N)
def branchSumsHelper(node, branchSums, current_sum):
    if not node:
        return
    new_sum = current_sum + node.value
    if node.left is None and node.right is None:
        branchSums.append(new_sum)
    if node.left is not None:
        branchSumsHelper(node.left, branchSums, new_sum)
    if node.right is not None:
        branchSumsHelper(node.right, branchSums, new_sum)