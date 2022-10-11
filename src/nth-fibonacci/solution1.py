# Time complexity - O(n)
# Space complexity - O(1)
def getNthFib(n):
    first = 0
    second= 1
    for _ in range(n-1):
        first, second = second, first + second
    return first
