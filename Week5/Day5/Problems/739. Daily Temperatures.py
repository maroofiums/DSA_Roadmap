from typing import List

def dailyTemperatures(temp: List[int]) -> List[int]:
    n = len(temp)
    res = [0] * n
    stack = []

    for i in range(n):
        while stack and temp[i] > temp[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev

        stack.append(i)

    return res

# Example Usage: 
temp: List[int] = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temp))
if (dailyTemperatures(temp) == [1,1,4,2,1,1,0,0]):
    print("test case passed✔")