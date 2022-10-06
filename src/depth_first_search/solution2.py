from collections import deque

# Time complexity - O(V+E)
# Space complexity - O(V)
def depthFirstSearch(root, array):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            array.append(node.name)
            queue.extendleft(reversed(node.children))
    return array
