class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if not stack:
                    return False

                curr = stack.pop()
                if mapping[curr] != char:
                    return False
        
        if len(stack) != 0:
            return False

        return True

        