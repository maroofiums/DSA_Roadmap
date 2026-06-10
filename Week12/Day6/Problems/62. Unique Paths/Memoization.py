def uniquePaths(m: int, n: int) -> int:

    memo = {(0,0):1}
    def solver(r,c):
        if (r,c) in memo:
            return memo[(r,c)]
        
        if r < 0 or c < 0 or r == m or c == n:
            return 0

        val = solver(r-1,c) + solver(r,c-1)

        memo[(r,c)] = val 
        return val

    return solver(m-1,n-1)

m: int = 3
n: int = 7

print(uniquePaths(m,n))
