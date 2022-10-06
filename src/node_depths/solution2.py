# Time complexity - O(n)
# Space complexity - average O(logn), worst O(n)
def nodeDepths(root):
    stack = [(root, 0)]
    total_depth = 0
    while stack:
        node, depth = stack.pop()
        if not node:
            continue
        total_depth += depth
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))

    return total_depth