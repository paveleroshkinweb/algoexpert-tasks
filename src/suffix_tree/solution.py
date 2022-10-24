class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Time complexity - O(n**2)
    def populateSuffixTrieFrom(self, string):
        for i in range(0, len(string)):
            tree = self.root
            for j in range(i, len(string)):
                if string[j] not in tree:
                    tree[string[j]] = {}
                tree = tree[string[j]]
            tree[self.endSymbol] = True 
    
    # Time complexity - O(n)
    def contains(self, string):
        tree = self.root
        for char in string:
            if char not in tree:
                return False
            tree = tree[char]
        return self.endSymbol in tree
