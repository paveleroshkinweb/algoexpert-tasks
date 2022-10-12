# Time complexity - O(n**2 + nlogn) -> O(n**2)
# Space complexity - O(1)
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[left] + array[right] + array[i]
            if current_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum > targetSum:
                right -= 1
            else:
                left += 1
    return triplets