class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        ans = left = 0
        
        for right in range(len(s)):
            if s[right] in unique:
                left = max(left, unique[s[right]] + 1)
            
            unique[s[right]] = right
            ans = max(ans, right - left + 1)
            
        return ans