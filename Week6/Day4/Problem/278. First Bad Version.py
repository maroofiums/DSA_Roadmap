def firstBadVersion(n: int) -> int:
    l, r = 1, n

    while l < r:
        mid = l + ((r - l) // 2)

        if isBadVersion(mid):
            r = mid
        else:
            l = mid + 1
    return l

def isBadVersion(version: int) -> bool:
    # Make this demo fuction
    return version >= 4
# Example usage:
n = 5
print(firstBadVersion(n))  # Output: 4
