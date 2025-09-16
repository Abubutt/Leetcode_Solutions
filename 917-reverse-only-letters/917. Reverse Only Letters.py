class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [letter for letter in s]
        size = len(s)
        left = 0
        right = size - 1

        while left < right:
            while left < right and not letters[left].isalpha():
                left += 1
            
            while left < right and not letters[right].isalpha():
                right -= 1

            letters[left], letters[right] = letters[right], letters[left]
            
            left += 1
            right -= 1

        return "".join(letters)

        
        