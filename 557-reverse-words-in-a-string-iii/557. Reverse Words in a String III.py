class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        ans = []

        for word in words:
            letters = [letter for letter in word]
            left = 0
            right = len(word) - 1

            while left <= right:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1

            ans.append("".join(letters))

        return " ".join(ans)
