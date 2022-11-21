# Time complexity - O(n**2)
# Space complexity - O(n)
def maxSumIncreasingSubsequence(array):
    subsolutions = [[array[i], -1] for i in range(len(array))]
    for i in range(len(array) - 2, -1, -1):
        for j in range(i+1, len(array)):
            if array[j] > array[i] and subsolutions[j][0] >= subsolutions[i][0]:
                subsolutions[i][0] = subsolutions[j][0] + array[i]
                subsolutions[i][1] = j
    max_subseq_idx = subsolutions.index(max(subsolutions, key=lambda item: item[0]))
    result = [subsolutions[max_subseq_idx][0], []]
    while max_subseq_idx != -1:
        result[1].append(array[max_subseq_idx])
        max_subseq_idx = subsolutions[max_subseq_idx][1]
    return result
