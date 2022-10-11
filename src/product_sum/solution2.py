# Time complexity - O(n)
# Space complexity - O(d), d - the greatest depth
def productSum(array):
    product_sum = 0
    product = 1
    depth=1
    stack = [(array, depth, product)]
    while stack:
        arr, depth, product = stack.pop()
        for item in arr:
            if isinstance(item, list):
                stack.append((item, depth+1, product * (depth+1)))
            else:
                product_sum += product * item
    return product_sum