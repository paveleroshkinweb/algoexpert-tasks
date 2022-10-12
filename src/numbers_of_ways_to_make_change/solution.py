# Time complexity - O(nd)
# Space complexity - O(n)
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    if n == 0:
        return 1
    if n < 0 or len(denoms) == 0:
        return 0
    element = denoms[0]
    ways = 0
    for i in range((n // element) + 1):
        ways += numberOfWaysToMakeChange(n - i * element, denoms[1:])
    return ways
