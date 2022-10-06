# Time complexity - O(nlogn)
# Space complexity - O(1)
def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    for idx in range(0, len(queries)-1):
        waiting_time += queries[idx] * (len(queries) - idx - 1)
    return waiting_time
