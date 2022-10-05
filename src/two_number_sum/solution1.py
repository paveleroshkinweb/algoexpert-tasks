# Time complexity - O(nlogn)
# Space complexity - O(n), potentially can be O(1) if array mutation is allowed
def twoNumberSum(array, target_sum):
    sorted_array = sorted(array)
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = sorted_array[left] + sorted_array[right]
        if current_sum == target_sum:
            return [sorted_array[left], sorted_array[right]]
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return []