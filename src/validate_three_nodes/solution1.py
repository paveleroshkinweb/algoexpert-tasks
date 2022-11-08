# Time complexity - O(d), d - depth
# Space complexity - O(1)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return checkNodeOne(nodeOne, nodeTwo, nodeThree) or checkNodeOne(nodeThree, nodeTwo, nodeOne)

    
def checkNodeOne(nodeOne, nodeTwo, nodeThree):
    current = nodeOne
    while current and current != nodeTwo:
        if current.value > nodeTwo.value:
            current = current.left
        else:
            current = current.right

    if not current:
        return False

    while current and current != nodeThree:
        if current.value > nodeThree.value:
            current = current.left
        else:
            current = current.right

    return current == nodeThree