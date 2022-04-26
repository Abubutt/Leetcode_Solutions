class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxWater = 0
        
        while start < end:
            L = min(height[start], height[end])
            W = end-start
            currentArea = L*W
            maxWater = max(maxWater, currentArea)
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
        return maxWater
    
    # 