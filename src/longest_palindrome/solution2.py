# Time complexity - O(n^2)
# Space complexity - O(n)
def longestPalindromicSubstring(string):
    if len(string) <= 1:
        return string
    longest_substr = (0, 0)
    for i in range(1, len(string)):
        left1, right1 = isPalindrome(string, i-1, i+1)
        left2, right2 = isPalindrome(string, i-1, i)
        if right1 - left1 + 1 > longest_substr[1] - longest_substr[0]:
            longest_substr = (left1, right1)
        if right2 - left2 + 1 > longest_substr[1] - longest_substr[0]:
            longest_substr = (left2, right2)
    return string[longest_substr[0]:longest_substr[1]+1]


def isPalindrome(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


print(longestPalindromicSubstring("abcaa"))