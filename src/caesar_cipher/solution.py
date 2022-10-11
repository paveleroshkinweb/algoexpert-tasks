# Time complexity - O(N)
# Space complexity - O(N)
def caesarCipherEncryptor(string, key):
    key = key % 26
    encrypted_string = [None] * len(string)
    for i, char in enumerate(string):
        code = (ord(char) + key)
        if code > 122:
            code = 96 + (code % 122)
        encrypted_string[i] = chr(code)
    return str(encrypted_string)
