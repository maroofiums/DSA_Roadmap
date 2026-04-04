def isPalindrome(s: str) -> bool:
    filtered = []

    for c in s:
        if c.isalnum():
            filtered.append(c.lower())
    return filtered == filtered[::-1]

# Example usage
print(isPalindrome("A man, a plan, a canal: Panama"))