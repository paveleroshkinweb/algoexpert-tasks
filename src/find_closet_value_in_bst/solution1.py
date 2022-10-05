# Time complexity - O(logN)
# Space complexity - O(logN)
def findClosestValueInBst(tree, target):
    if not tree:
        return None
    root_diff = tree.value - target
    subsolution = None

    if root_diff == 0:
        return tree.value
    elif root_diff > 0:
        subsolution = findClosestValueInBst(tree.left, target)
    elif root_diff < 0:
        subsolution = findClosestValueInBst(tree.right, target)

    if subsolution is None:
        return tree.value
    elif abs(root_diff) < abs(subsolution - target):
        return tree.value
    else:
        return subsolution
