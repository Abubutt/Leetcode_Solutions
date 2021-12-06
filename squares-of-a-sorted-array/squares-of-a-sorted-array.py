class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0]*n
        c=n-1
        j=n-1
        i = 0
        while i<=j:
            if abs(nums[i]) > abs(nums[j]):
                res[c] = nums[i]*nums[i]
                i+=1
            else:
                res[c] = nums[j]*nums[j]
                j-=1
            c-=1
        return res
        
        
     