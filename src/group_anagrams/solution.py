from collections import defaultdict

# Time complexity - O(n*w*logn)
# Space complexity - O(n*w)
def groupAnagrams(words):
    sorted_words = ["".join(sorted(word))  for word in words]
    groups = defaultdict(lambda: [])
    for idx, word in enumerate(words):
        sorted_word = sorted_words[idx]
        groups[sorted_word].append(word)
    return list(groups.values())