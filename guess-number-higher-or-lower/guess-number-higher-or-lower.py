# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while True:
            mid = low + (high-low)//2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                high = mid -1
            else:
                low = mid + 1
                
