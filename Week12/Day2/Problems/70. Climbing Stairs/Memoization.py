def climbStairs(n: int) -> int:

    memo = {1:1,2:2}

    def dfs(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = dfs(n-1) + dfs(n-2)

        return memo[x]

    return dfs(n)

n: int = 3
print(climbStairs(n))