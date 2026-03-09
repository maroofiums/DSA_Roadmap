def longestPalindrome(s:str) -> int:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_count = False
    for count in char_count.values():
        length += (count // 2) * 2
        if count % 2 == 1:
            odd_count = True

    return length + (1 if odd_count else 0)

# Example usage:
s = "abccccdd"
print(longestPalindrome(s))  # Output: 7
