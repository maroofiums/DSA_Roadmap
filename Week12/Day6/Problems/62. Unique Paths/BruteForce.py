def uniquePaths(m: int, n: int) -> int:
    def solver(r,c):
        if r == c == 0:
            return 1
        
        if r < 0 or c < 0 or r == m or c == n:
            return 0

        return solver(r-1,c) + solver(r,c-1)

    return solver(m-1,n-1)

m: int = 3
n: int = 7

print(uniquePaths(m,n))
