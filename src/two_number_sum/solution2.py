from collections import defaultdict

# Time complexity - O(n)
# Space complexity - O(n)
def twoNumberSum(array, target_sum):
    numbers_map = defaultdict(lambda: [])
    for idx, item in enumerate(array):
        numbers_map[item].append(idx)
    for idx, item in enumerate(array):
        diff = target_sum - item
        bucket = numbers_map[diff]
        if bucket and bucket[0] > idx or len(bucket) > 1:
            return [item, diff]
    return []