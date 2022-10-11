# Time complexity - O(n**2)
# Space complexity - O(1)
def selectionSort(array):
    for i in range(len(array)):
        current_min = i
        for j in range(i+1, len(array)):
            if array[j] < array[current_min]:
                current_min = j
        array[i], array[current_min] = array[current_min], array[i]
    return array
