# Time complexity - O(n*2^n)
# Space complexity - O(2^n)
def powerset(array):
    if len(array) == 0:
        return [[]]
    last_element = array.pop()
    subsets = powerset(array)
    for idx in range(len(subsets)):
        subsets.append(subsets[idx] + [last_element])
    return subsets
