# Time complexity - O(n)
# Space complexity - O(1)
def kadanesAlgorithm(array):
    max_subsum = array[0]
    current_max = max_subsum
    for idx in range(1, len(array)):
        current_max = max(current_max+array[idx], array[idx])
        max_subsum = max(current_max, max_subsum)
    return max_subsum
