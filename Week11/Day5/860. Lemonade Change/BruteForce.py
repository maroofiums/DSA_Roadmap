from typing import List

def lemonadeChange(bills: List[int]) -> bool:

    def dfs(i,five,ten):
        if i == len(bills):
            return True
        
        bill = bills[i]

        if bill == 5:
            return dfs(i+1,five+1,ten)

        elif bill == 10:
            if five == 0:
                return False
            return dfs(i+1,five-1,ten+1)
        
        else:
            if ten > 0 and five > 0:
                return dfs(i+1,five-1,ten-1)
            elif five >= 3:
                return dfs(i+1,five-3,ten)
            
            return False

    return dfs(0,0,0)

bills: List[int] = [5,5,5,10,20]

print(lemonadeChange(bills))

