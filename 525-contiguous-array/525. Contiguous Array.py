from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        countZeros = defaultdict(int)
        currSum = 0
        
        maxLength = 0
        
        countZeros[0] = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                currSum -= 1
            
            else:
                currSum += nums[i]

            if currSum in countZeros:
                maxLength = max(maxLength, i-countZeros[currSum])
            else:
                countZeros[currSum] = i 
                
        return maxLength
                
            
        