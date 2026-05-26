from typing import List

def solveNQueens(n:int) -> List[List[int]]:
    col = set()
    posDig = set()
    negDig = set()

    res = []

    board = [["."] * n for i in range(n)]

    def backtrack(r=0):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return 
        
        for c in range(n):
            if c in col or (r + c) in posDig or (r - c) in negDig:
                continue

            col.add(c)
            posDig.add(r + c)
            negDig.add(r - c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDig.remove(r + c)
            negDig.remove(r - c)
            board[r][c] = "."

    backtrack()
    return res

# Example Usage:

if __name__ == "__main__":
    n:int = 4

    print(solveNQueens(4))