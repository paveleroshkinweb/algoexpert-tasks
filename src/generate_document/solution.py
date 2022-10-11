from collections import defaultdict

# Time complexity - O(n+m)
# Space complexity - O(c), c - unique charecters
def generateDocument(characters, document):
    # Write your code here.
	counter = defaultdict(lambda: 0)
	for char in characters:
		counter[char] += 1
	for char in document:
		if counter[char] > 0:
			counter[char] -= 1
		else:
			return False
	return True
