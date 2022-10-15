# Time complexity - O(d), d - depth
# Space complexity - O(1)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth1 = getDepth(descendantOne)
    depth2 = getDepth(descendantTwo)
    current1 = descendantOne
    current2 = descendantTwo
    if depth1 > depth2:
        current1 = moveUp(current1, depth1-depth2)
    else:
        current2 = moveUp(current2, depth2-depth1)
    while current1 != current2:
        current1 = current1.ancestor
        current2 = current2.ancestor
    return current1

def getDepth(node):
    depth = 1
    current = node
    while current:
        depth += 1
        current = current.ancestor
    return depth


def moveUp(node, diff):
    for i in range(diff):
        node = node.ancestor
    return node