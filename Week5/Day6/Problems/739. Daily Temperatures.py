from typing import List

def dailyTemperatures(temperature:List[int]) -> List[int]:
    n = len(temperature)
    res = [0] * n
    stack = []

    for i in range(n):
        while stack and temperature[stack[-1]] < temperature[i]:
            prev = stack.pop()
            res[prev] = i - prev

        stack.append(i) 
        
    return res

# Example Usage: 
temperatures: List[int] = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

if (dailyTemperatures(temperatures) == [1,1,4,2,1,1,0,0]):
    print("Test Case Passed✔")