class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left = count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        ans = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1

            if s[left] in vowels:
                count -= 1
            left += 1

            ans = max(ans, count)
        
        return ans
        