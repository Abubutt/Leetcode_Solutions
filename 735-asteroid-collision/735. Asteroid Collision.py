class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        equal = False

        for asteriod in asteroids:
            equal = False
            if not stack:
                stack.append(asteriod)
                continue

            while stack and (stack[-1] > 0 and asteriod < 0) and abs(asteriod) >= abs(stack[-1]):
                if abs(asteriod) == abs(stack[-1]):
                    stack.pop()
                    equal = True
                    break
                stack.pop()

            if equal:
                continue
            
            if not stack:
                stack.append(asteriod)
                continue

            if stack and (stack[-1] < 0 and asteriod > 0):
                stack.append(asteriod)
                continue

            if stack and ((stack[-1] < 0 and asteriod < 0) or (stack[-1] > 0 and asteriod > 0)):
                stack.append(asteriod)


        return stack
            

        