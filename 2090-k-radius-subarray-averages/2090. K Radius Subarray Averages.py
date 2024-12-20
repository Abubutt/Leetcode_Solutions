class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum = [nums[0]]
        averages = []
        size = len(nums)
        radiusSize = k*2+1
        
        for i in range(1, size):
            prefixSum.append(nums[i] + prefixSum[-1])
            
        
        for i in range(size):
            if i-k < 0 or i+k >= size:
                averages.append(-1)
            elif i-k == 0:
                averages.append(prefixSum[i+k] // radiusSize)
            else:
                currSum = prefixSum[i+k] - prefixSum[i-k] + nums[i-k]
                averages.append(currSum // radiusSize)
                
        return averages