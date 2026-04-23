from typing import List

def dailtTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev

        stack.append(i)

    return res

# Example Usage: 
temperatures: List[int] = [73,74,75,71,69,72,76,73]
print(dailtTemperatures(temperatures))
if (dailtTemperatures(temperatures) == [1,1,4,2,1,1,0,0]):
    print("All Test Case Passed✔")