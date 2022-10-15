from math import factorial

# Time complexity - O(n)
# Space complexity - O(1)
def numberOfWaysToTraverseGraph(width, height):
    ways = factorial(width + height - 2) / (factorial(width - 1) * factorial(height - 1))
    return ways