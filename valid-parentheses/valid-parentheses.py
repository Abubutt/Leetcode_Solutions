class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "(" or p =="{" or p == "[":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                elif p == ")" and stack[-1] == "(":
                    stack.pop()
                elif p == "}" and stack[-1] == "{":
                    stack.pop()
                elif p == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False