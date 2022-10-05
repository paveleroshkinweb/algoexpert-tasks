# Time complexity - O(nlogn)
# Space complexity - O(n), potentially can be O(1) if array mutation is allowed
def nonConstructibleChange(coins):
    current_sum = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        if coin > current_sum + 1:
            return current_sum + 1
        current_sum += coin
    return current_sum + 1
