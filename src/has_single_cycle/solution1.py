# Time complexity - O(n)
# Space complexity - O(n)
def hasSingleCycle(array):
    visited = set()
    current_idx = 0
    while len(visited) < len(array):
        if current_idx in visited:
            return False
        visited.add(current_idx)
        current_idx = (current_idx + array[current_idx]) % len(array) 
    return current_idx == 0

