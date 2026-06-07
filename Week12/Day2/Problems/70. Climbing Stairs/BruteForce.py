def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    return climbStairs(n-1) + climbStairs(n-2)

n: int = 3
print(climbStairs(n))