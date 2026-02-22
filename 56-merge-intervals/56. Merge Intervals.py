class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for interval in intervals:
            start, end = interval
            if stack and stack[-1][1] >= start:
                pastStart, pastEnd = stack.pop()
                stack.append([pastStart, max(pastEnd, end)])
            else:
                stack.append(interval)

        return stack

        # [1,4] [2, 3]
        