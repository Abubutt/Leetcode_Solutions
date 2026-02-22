class Solution:
    def reverse(self, x: int) -> int:
        if 0 <= x < 10:
            return x
            
        ans = 0
        digits = []
        isNegative = False

        if x < 0:
            isNegative = True

        if isNegative:
            x *= -1

        while x > 0:
            digit = x % 10
            x = x // 10
            digits.append(digit)

        startIdx = 0

        while digits[startIdx] == 0:
            startIdx += 1

        power = len(digits) - startIdx - 1

        for i in range(startIdx, len(digits)):
            digit = digits[i]
            ans += digit * (10 ** power)
            power -= 1

        if isNegative:
            ans *= -1

        lowBound = -2 ** 31
        highBound = 2 ** 31 - 1

        if ans < lowBound or ans > highBound:
            return 0

        return ans

        

        
        