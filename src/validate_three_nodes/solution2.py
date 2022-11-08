# Time complexity - O(d), d - depth
# Space complexity - O(1)
def validateThreeNodes(node1, node2, node3):
    if node2.value > node1.value and node2.value > node3.value:
        if node1.value < node3.value:
            return check(node1, node2, node3)
        return check(node3, node2, node1)
    
    elif node2.value < node1.value and node2.value < node3.value:
        if node1.value > node3.value:
            return check(node1, node2, node3)
        return check(node3, node2, node1)
    
    else:
        return check(node1, node2, node3) or check(node3, node2, node1)


def check(node1, node2, node3):
    current = node1
    while current and current != node2:
        if current == node3:
            return False
        if current.value > node2.value:
            current = current.left
        else:
            current = current.right

    if not current:
        return False

    while current and current != node3:
        if current.value > node3.value:
            current = current.left
        else:
            current = current.right

    return current == node3