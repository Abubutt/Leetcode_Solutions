class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        combined = s + s
        for i in range(len(combined)):
            if combined[i:len(s) + i] == goal:
                return True

        return False