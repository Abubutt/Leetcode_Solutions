class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            equal = False
            while stack and (stack[-1] > 0 and asteroids[i] < 0) and abs(asteroids[i]) >= abs(stack[-1]):
                if abs(asteroids[i]) == abs(stack[-1]):
                    equal = True
                    stack.pop()
                    break
                stack.pop()
            if not stack or (stack and ((stack[-1] > 0 and asteroids[i] > 0) or (stack[-1] < 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] > 0))):
                if not equal:
                    stack.append(asteroids[i])

        return stack

-2
-2