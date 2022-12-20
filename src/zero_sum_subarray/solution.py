# Time complexity - O(n)
# Space complexity - O(n)
def zeroSumSubarray(nums):
    subsums = set()
    current_sum = 0
    for n in nums:
        current_sum += n

        if current_sum == 0 or current_sum in subsums:
            return True

        subsums.add(current_sum)

    return False
