class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLength = currCost = left = 0

        for right in range(len(s)):
            currCost += abs(ord(s[right]) - ord(t[right]))
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            maxLength = max(maxLength, right-left+1)

        return maxLength

        