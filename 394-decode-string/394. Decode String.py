class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "]":
                string = []
                digits = []
                while stack and not stack[-1].isdigit():
                    last_ch = stack.pop()
                    if last_ch.isalpha():
                        string.append(last_ch)
                
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())

                digits.reverse()
                string.reverse()

                freq = int("".join(digits))
                string = "".join(string)
                stack.append(string * freq)
            else:
                stack.append(ch)

        return "".join(stack)


                
        