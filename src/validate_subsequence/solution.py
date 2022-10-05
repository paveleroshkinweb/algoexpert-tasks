# Time complexity O(N)
# Space complexity O(1)
def isValidSubsequence(array, sequence):
    sequence_index = 0
    for item in array:
        if item == sequence[sequence_index]:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    return False