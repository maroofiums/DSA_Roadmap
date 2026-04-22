def isValid(s: str) -> bool:
    stack = []
    hashmap = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for c in s:
        if c in hashmap:
            if not stack or stack.pop() != hashmap[c]:
                return False

        else:
            stack.append(c)

    
    return not stack

# Example Usage: 
s: str = "()[]{}"
print(isValid(s))