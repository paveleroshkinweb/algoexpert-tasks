# Time complexity - O(n)
# Space complexity - average O(logn), worst O(n)
def nodeDepths(root):
    return nodeDepthsHelper(root, 0) 


def nodeDepthsHelper(node, depth):
    if not node:
        return 0
    
    if node.left is None and node.right is None:
        return depth

    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)