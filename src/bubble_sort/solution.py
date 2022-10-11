def bubbleSort(array):
    for i in range(1, len(array)):
        swap = False
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if not swap:
            break
    return array
