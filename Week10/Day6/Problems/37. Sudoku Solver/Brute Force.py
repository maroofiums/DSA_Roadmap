from typing import List

def solveSudoku(board: List[List[str]]) -> List[List[str]]:
    def isValid(board,row,col,num_char):
        for r in range(9):
            if board[r][col] == num_char:
                return False
        
        for c in range(9):
            if board[row][c] == num_char:
                return False
            
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row,box_row+3):
            for c in range(box_col,box_col+3):
                if board[r][c] == num_char:
                    return False
        return True
    
    def solver(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in range(1,10):
                        num_char = str(num)
                        if isValid(board,r,c,num_char):
                            board[r][c] = num_char
                            if solver(board):
                                return True
                            else:
                                board[r][c] = "."
                
                    return False
        return True
    
    solver(board)

    return board

board: List[List[str]] = [
        [".",".",".",".",".",".",".",".","."],
        [".","9",".",".","1",".",".","3","."],
        [".",".","6",".","2",".","7",".","."],
        [".",".",".","3",".","4",".",".","."],
        ["2","1",".",".",".",".",".","9","8"],
        [".",".",".",".",".",".",".",".","."],
        [".",".","2","5",".","6","4",".","."],
        [".","8",".",".",".",".",".","1","."],
        [".",".",".",".",".",".",".",".","."]
    ]
ans = solveSudoku(board)

print("[")
for res in ans:
    print(" ",res,",")
print("]")
