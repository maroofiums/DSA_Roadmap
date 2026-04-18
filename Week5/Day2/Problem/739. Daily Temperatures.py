from typing import List

def dailyTemperatures(temp: List[int]) -> List[int]:
    n = len(temp)
    ans = [0] * n
    stack = []

    for i in range(n):
        while stack and temp[i] > temp[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev

        stack.append(i)

    return ans

# Example Usage:
temp: List[int] = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temp))
