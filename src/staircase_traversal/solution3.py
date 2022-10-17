# Time complexity - O(h)
# Space complexity - O(h)
def staircaseTraversal(height, maxSteps):
    cache = [1, 1]
    for i in range(2, height + 1):
        if i <= maxSteps:
            cache.append(2 * cache[i-1])
        else:
            cache.append(2 * cache[i-1] - cache[i-maxSteps-1])
    return cache[-1]
