class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        currMax = 0
        for i in range(len(height)):
            maxL[i] = currMax
            currMax = max(currMax, height[i])

        currMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = currMax
            currMax = max(currMax, height[i])

        ans = 0

        for i in range(len(height)):
            amount = max(0, min(maxL[i], maxR[i]) - height[i])
            ans += amount

        return ans
        