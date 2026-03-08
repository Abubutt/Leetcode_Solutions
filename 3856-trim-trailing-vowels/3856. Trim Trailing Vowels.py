class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        stack = [ch for ch in s]
        vowels = {"a", "e", "i", "o", "u"}

        while stack and stack[-1] in vowels:
            stack.pop()

        return "".join(stack)
        