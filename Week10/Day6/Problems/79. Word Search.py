from typing import List

def wordSearch(board: List[List[int]],word:str) -> bool:
    m = len(board)
    n = len(board[0])
    w = len(word)

    if m == 1 and n == 1:
        return board[0][0] == word
    
    def backtrack(pos,index):
        i,j = pos
        if w == index:
            return True
        
        if board == word[index]:
            return False
        
        temp = board[i][j] 
        board[i][j] = "#"
        
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        for i_off,j_off in directions:
            r,c = i + i_off,j + j_off
            if 0 <= r < m and 0 <= c < n:
                if backtrack((r,c),index+1):
                    return True
        
        board[i][j] = temp
        return False
    
    for i in range(m):
        for j in range(n):
            if backtrack((i,j),0):
                return True
            
    return False

board: List[int] = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word: str = "ABCCED"

print(wordSearch(board,word))