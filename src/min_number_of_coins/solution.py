# Time complexity - O(nd)
# Space complexity - O(n)
def minNumberOfCoinsForChange(n, denoms):
	return minNumberOfCoinsForChangeHelper(n, denoms, 0, 0)


def minNumberOfCoinsForChangeHelper(n, denoms, current_number, denom_index):
	if n == 0:
		return current_number
	if denom_index >= len(denoms):
		return -1
	denom = denoms[denom_index]
	min_coins = float('inf')
	for i in range((n // denom) + 1):
		new_change = n - i * denom
		new_current_number = current_number + i 
		if new_current_number >= min_coins or new_change < 0:
			break
		ways = minNumberOfCoinsForChangeHelper(new_change, denoms, new_current_number, denom_index+1)
		if ways > 0:
			min_coins = min(min_coins, ways)
	return -1 if min_coins == float('inf') else min_coins
