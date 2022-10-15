# Time complexity - O(v+e)
# Space complexity - O(v)
def breadthFirstSearch(start_node, array):
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        array.append(node.name)
        queue.extend(node.children)
    return array
