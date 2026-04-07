def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    res = 0

    for i in range(n):
        count = [0] * 26
        max_freq = 0

        for j in range(i, n):
            idx = ord(s[j]) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])

            window_size = j - i + 1
            if window_size - max_freq <= k:
                res = max(res, window_size)

    return res

print(characterReplacement("ABABBAC",2))