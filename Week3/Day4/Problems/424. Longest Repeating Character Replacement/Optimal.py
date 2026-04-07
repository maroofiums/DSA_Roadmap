def charaterReplacement(s,k):
    win = {}
    l = max_len = 0

    for r in range(len(s)):
        win[s[r]] = win.get(s[r],0) + 1

        if ((r - l + 1) - max(win.values())) > k:
            win[s[l]] -= 1
            l += 1

        max_len = max(max_len,r-l+1)
    return max_len

print(charaterReplacement("ABABBAC",2))