class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = [char for char in word]

        for i in range(len(word)):
            if word[i] == ch:
                left = 0
                right = i
                while left < right:
                    ans[left], ans[right] = ans[right], ans[left]
                    left += 1
                    right -= 1
                break
        
        return "".join(ans)
        