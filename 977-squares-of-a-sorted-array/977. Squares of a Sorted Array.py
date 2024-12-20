class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        
        minVal = nums[0]**2
        minIndex = 0
        
        for i in range(len(nums)):
            if nums[i]**2 < minVal:
                minVal = nums[i]**2
                minIndex = i
                
        ans.append(minVal)
  
        l = minIndex - 1
        r = minIndex + 1
        
        while l >= 0 and r < len(nums):
            if nums[l] ** 2 < nums[r] ** 2:
                ans.append(nums[l] ** 2)
                l-=1
            else:
                ans.append(nums[r] ** 2)
                r+=1
                
        while l >= 0:
            ans.append(nums[l] ** 2)
            l-=1
        
        while r < len(nums):
            ans.append(nums[r]**2)
            r+=1
        
        return ans