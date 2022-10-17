# Time complexity - O(n)
# Space complexity - O(n)
def balancedBrackets(string):
    brackets_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    open_brackets = set(brackets_map.values())
    stack = [string[0]]
    for el in string[1:]:
        if el in open_brackets:
            stack.append(el)
        if el in brackets_map:
            last_bracket = stack.pop()
            if brackets_map[el] != last_bracket:
                return False
    return len(stack) == 0
