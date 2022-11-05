# Time complexity - O(n)
# Space complexity - O(1)
def minRewards(scores):
    assert len(scores) > 0
    if len(scores) == 1:
        return 1
    if len(scores) == 2:
        return 3
    is_up = scores[0] < scores[1]
    idx = 0
    min_rewards = 0
    prev_left = 0
    jumps = 0
    while idx < len(scores) - 1:
        if is_up:
            new_idx = count_up(scores, idx)
            min_rewards += count(new_idx - idx)
            prev_left = new_idx - idx
            if is_local_min(scores, idx):
                jumps += 1
        else:
            new_idx = count_down(scores, idx)
            min_rewards += count(new_idx - idx) + max(prev_left, new_idx - idx) + 1 
            prev_left = 0
        is_up = not is_up
        idx = new_idx
    if scores[-1] > scores[-2]:
        min_rewards += prev_left + 1
    return min_rewards - jumps


def is_local_min(scores, idx):
    return idx != 0 and scores[idx] < scores[idx-1] and scores[idx] < scores[idx+1]


def count_up(scores, idx):
    while idx < len(scores) - 1 and scores[idx] < scores[idx+1]:
        idx += 1
    return idx


def count_down(scores, idx):
    while idx < len(scores) - 1 and scores[idx] > scores[idx+1]:
        idx += 1
    return idx


def count(n):
    return (n * (n+1) // 2)