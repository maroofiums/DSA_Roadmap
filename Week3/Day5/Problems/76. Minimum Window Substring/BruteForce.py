def minWindow(s: str, t: str):
    def contains(sub: str, t: str) -> bool:
        for c in t:
            if sub.count(c) < t.count(c):
                return False
        return True
    n = len(s)
    res = ""
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if contains(sub, t) and (res == "" or len(sub) < len(res)):
                res = sub
    return res

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"