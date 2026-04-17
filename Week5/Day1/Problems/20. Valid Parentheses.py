def isValid(s: str) -> bool:
    stack = []
    pairs = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
            
        else:
            if not stack:
                return False
                
            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0

# Example Usage:
s: str = "()[]{}"
print(isValid(s))