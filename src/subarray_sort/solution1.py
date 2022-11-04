# Time complexity - O(n)
# Space complexity - O(1)
def subarraySort(array):
    subarray_idx = [-1, -1]
    currentMaxWindow = float('-inf')
    currentMinWindow = float('inf')
    for i in range(0, len(array)):
        if wrongOrder(array, i) or array[i] < currentMaxWindow:
            subarray_idx[1] = i
            currentMinWindow = min(currentMinWindow, array[i])    
        currentMaxWindow = max(currentMaxWindow, array[i])

    if subarray_idx[1] == -1:
        return subarray_idx

    subarray_idx[0] = 0
    while array[subarray_idx[0]] <= currentMinWindow:
        subarray_idx[0] += 1
    return subarray_idx


def wrongOrder(array, i):
    if i == 0:
        return array[i] > array[i+1]
    if i == len(array) - 1:
        return array[i] < array[i-1]
    return array[i-1] > array[i] or array[i] > array[i+1]
