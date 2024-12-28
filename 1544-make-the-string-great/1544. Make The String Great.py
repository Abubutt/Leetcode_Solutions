class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1].lower() == char.lower() and ord(char) != ord(stack[-1]):
                _ = stack.pop()
            else:
                stack.append(char)
                
        return "".join(stack)
        