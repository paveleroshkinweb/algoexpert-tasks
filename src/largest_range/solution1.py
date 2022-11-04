# Time complexity - O(nlogn)
# Space complexity - O(1)
def largestRange(array):
    array.sort()
    largest_range = [0, 0]
    current_range = [0, 0]
    for i in range(1, len(array)):
        if array[i] == array[i-1] + 1:
            current_range[1] = i
        if current_range[1] - current_range[0] > largest_range[1] - largest_range[0]:
            largest_range = current_range[:]
        if array[i] != array[i-1] + 1 and array[i] != array[i-1]:
            current_range = [i, i]
    return [array[largest_range[0]], array[largest_range[1]]]
