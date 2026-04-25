pick = 6   # hidden number


def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1


# Run
obj = Solution()
print(obj.guessNumber(10))