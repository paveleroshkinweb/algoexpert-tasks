# Time complexity - O(d), d - depth
# Space complexity - O(d)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    path1 = set()
    current = descendantOne
    while current:
        path1.add(current)
        current = current.ancestor
    
    current = descendantTwo
    while current:
        if current in path1:
            return current
        current = current.ancestor
    
    return topAncestor