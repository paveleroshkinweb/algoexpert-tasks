# Time complexity - O(n)
# Space complexity - O(d), d - the greatest depth
def productSum(array, depth=1):
    product_sum = 0
    for item in array:
        if isinstance(list, array):
            product_sum += (depth+1) * productSum(item, depth=depth+1)
        else:
            product_sum += item
    return product_sum