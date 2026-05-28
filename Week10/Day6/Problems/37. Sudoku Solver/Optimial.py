from typing import List

def solveSudoku(board:List[List[str]]) -> List[List[str]]:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxs = [set() for _ in range(9)]

    empty = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                empty.append((r,c))
            
            else:
                num = board[r][c]

                rows[r].add(num)
                cols[c].add(num)

                box_id = (r // 3) * 3 + (c // 3)

                boxs[box_id].add(num)

    def backtrack(index = 0):
        if index == len(empty):
            return True
        r,c = empty[index]

        box_id = (r // 3) * 3 + (c // 3)

        for num in range(1,10):
            num = str(num)
            if (num not in rows[r] 
                and num not in cols[c] 
                and num not in boxs[box_id]
            ):
                
                board[r][c] = num

                rows[r].add(num)
                cols[c].add(num)
                boxs[box_id].add(num)

                if backtrack(index + 1):
                    return True
                
                board[r][c] = "."

                rows[r].remove(num)
                cols[c].remove(num)
                boxs[box_id].remove(num)
        
        return False


    backtrack()

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
