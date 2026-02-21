class Solution:
    def trap(self, height: List[int]) -> int:
        # maxL = [0] * len(height)
        # maxR = [0] * len(height)

        # currMax = 0
        # for i in range(len(height)):
        #     maxL[i] = currMax
        #     currMax = max(currMax, height[i])

        # currMax = 0
        # for i in range(len(height) - 1, -1, -1):
        #     maxR[i] = currMax
        #     currMax = max(currMax, height[i])

        # ans = 0

        # for i in range(len(height)):
        #     amount = max(0, min(maxL[i], maxR[i]) - height[i])
        #     ans += amount

        # return ans

        left = ans = 0
        right = len(height) - 1
        maxL = maxR = 0

        while left < right:
            if height[left] < height[right]:
                maxL = max(maxL, height[left])
                ans += maxL - height[left]
                left += 1
            else:
                maxR = max(maxR, height[right])
                ans += maxR - height[right]
                right -= 1
        
        return ans