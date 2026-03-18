from collections import Counter

def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
        
    need = Counter(t)
    window = {}
    
    have = 0
    need_count = len(need)
        
    res = [-1, -1]
    res_len = float("inf")
        
    l = 0
        
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
            
        if c in need and window[c] == need[c]:
            have += 1
            
        # When window is valid
        while have == need_count:
            # Update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            # Shrink from left
            window[s[l]] -= 1
            
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
                
            l += 1
        
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

# Example Usage
s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))