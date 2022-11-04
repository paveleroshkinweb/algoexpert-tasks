# Time complexity - O(n)
# Space complexity - O(n)
def largestRange(array):
    members = set(array)
    largest_range = [0, 0]
    while members:
        element = members.pop()
        
        right_diff = 1
        while element + right_diff in members:
            members.remove(element + right_diff)
            right_diff += 1
        
        left_diff = -1
        while element + left_diff in members:
            members.remove(element + left_diff)
            left_diff -= 1
        
        left_border = element + left_diff + 1
        right_border = element + right_diff - 1
        if right_border - left_border >= largest_range[1] - largest_range[0]:
            largest_range = [left_border, right_border] 
    return largest_range