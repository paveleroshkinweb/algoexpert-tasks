# Time complexity - O(n)
# Space complexity - O(d), d - depth
def invertBinaryTree(tree):
    if not tree:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree