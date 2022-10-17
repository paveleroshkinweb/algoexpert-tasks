# Time complexity - O(m*h)
# Space complexity - O(h)
def staircaseTraversal(height, maxSteps):
    cache = [1]
    for i in range(1, height + 1):
        current_ways = 0
        for j in range(i - 1, max(-1, i - maxSteps - 1), -1):
            current_ways += cache[j]
        cache.append(current_ways)
    return cache[-1]
