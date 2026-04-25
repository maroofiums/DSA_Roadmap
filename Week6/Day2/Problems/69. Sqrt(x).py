def MySqrt(x: int) -> int:
    if x < 2:
        return x

    l, r = 1, x//2
    ans = 0

    while l <= r:
        mid = l + (r - l) // 2

        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

# Example usage:
print(MySqrt(4))  # Output: 2
print(MySqrt(8))  # Output: 2
print(MySqrt(0))  # Output: 0