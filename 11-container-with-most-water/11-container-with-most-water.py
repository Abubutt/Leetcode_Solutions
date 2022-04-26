class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxWater = 0
        
        while start < end: # 0(n)
            length = min(height[start], height[end]) # 0(2)
            width = end-start
            currentArea = length*width
            maxWater = max(maxWater, currentArea) # 0(2)
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
        return maxWater
    # time complexity: 0(4n) --> 0(n)