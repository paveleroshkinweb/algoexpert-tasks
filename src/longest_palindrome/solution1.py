# Time complexity - O(n^3)
# Space complexity - O(n)
def longestPalindromicSubstring(string):
    if len(string) <= 1:
        return string
    longest_substr = (0, 1)
    for i in range(1, len(string)+1):
        for j in range(0, len(string)-i+1):
            if isPalindrome(string, j, j+i-1):
                if longest_substr[1] - longest_substr[0] < i:
                    longest_substr = (j, j+i)
    return string[longest_substr[0]:longest_substr[1]]


def isPalindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
