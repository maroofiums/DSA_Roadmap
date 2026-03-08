def reverseString(s:int) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Example usage:
s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]