# Time complexity - O(n)
# Space complexity - O(n)
def firstDuplicateValue(array):
    used = set()
    for element in array:
        if element in used:
            return element
        used.add(element)
    return -1
