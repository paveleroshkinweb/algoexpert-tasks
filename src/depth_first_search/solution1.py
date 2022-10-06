# Time complexity - O(V+E)
# Space complexity - O(V)
def depthFirstSearch(node, array):
    if not node:
        return
    array.append(node.name)
    for child in node.children:
        depthFirstSearch(child, array)
    return array