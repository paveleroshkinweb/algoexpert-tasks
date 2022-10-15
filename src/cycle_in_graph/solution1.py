# Time complexity - O(v+e)
# Space complexity - O(v)
def cycleInGraph(edges):
    not_visited = set(range(len(edges)))
    colors = [False] * len(edges)
    while not_visited:
        vertex = not_visited.pop()
        not_visited.add(vertex)
        if is_cycle(vertex, edges, not_visited, colors):
            return True
    return False


def is_cycle(vertex, edges, not_visited, colors):
    if colors[vertex]:
        return True
    if vertex not in not_visited:
        return False
    colors[vertex] = True
    not_visited.remove(vertex)
    for child in edges[vertex]:
        if is_cycle(child, edges, not_visited, colors):
            return True
    colors[vertex] = False
    return False
