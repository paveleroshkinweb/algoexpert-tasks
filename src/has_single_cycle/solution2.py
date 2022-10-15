# Time complexity - O(n)
# Space complexity - O(1)
def hasSingleCycle(array):
    current_idx = 0
    visited = 0
    while visited < len(array):
        if visited > 0 and current_idx == 0:
            return False
        visited += 1
        current_idx = (current_idx + array[current_idx]) % len(array)
    return current_idx == 0
