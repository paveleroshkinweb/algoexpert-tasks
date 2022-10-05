# Time complexity - O(logN)
# Space complexity - O(1)
def findClosestValueInBst(tree, target):
    if not tree:
        return None
    closest = tree.value
    current = tree
    while current:
        diff = current.value - target
        if diff == 0:
            return current.value
        elif abs(diff) < abs(closest - target):
            closest = current.value
        elif diff > 0:
            current = current.left
        else:
            current = current.right
    return closest