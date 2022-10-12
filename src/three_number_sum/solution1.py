from collections import defaultdict

# Time complexity - O(n**2 + n + klogk) -> O(n**2)
# Space complexity - O(n)
def threeNumberSum(array, targetSum):
    cache = defaultdict(lambda: -1)
    triplets = []
    for idx, element in enumerate(array):
        cache[element] = idx
    for i in range(0, len(array) - 2):
        for j in range(i+1, len(array) - 1):
            diff = targetSum - array[i] - array[j]
            value_from_cache = cache[diff]
            if value_from_cache > j:
                triplets.append(sorted([array[i], array[j], diff]))
    return sorted(triplets, key=lambda x: (x[0], x[1]))
