class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        letters = [letter for letter in word]
        size = len(letters)
        
        for right in range(size):
            if letters[right] == ch:
                i = 0
                j = right

                while i < j:
                    letters[i], letters[j] = letters[j], letters[i]
                    i += 1
                    j -= 1

                break
        
        return "".join(letters)
        