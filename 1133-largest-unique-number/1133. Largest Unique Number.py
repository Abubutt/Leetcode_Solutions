from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largestNum = -1
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            
            
        for key, val in count.items():
            if val == 1 and key > largestNum:
                largestNum = key
        
        return largestNum
        
        