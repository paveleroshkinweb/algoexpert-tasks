# Time complexity - O(n * n!)
# Space complexity - O(n * n!),
def getPermutations(array):
    if len(array) == 0:
        return []
    permutations = []
    generatePermutations(0, array, permutations)
    return permutations


def generatePermutations(idx, array, permutations):
    if idx == len(array) - 1:
        permutations.append(array)
        return
    for i in range(idx, len(array)):
        copy = array[:]
        copy[idx], copy[i] = copy[i], copy[idx]
        generatePermutations(idx+1, copy, permutations)
