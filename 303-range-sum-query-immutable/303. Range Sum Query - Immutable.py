class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]
        self.size = len(nums)
        for i in range(1, self.size):
            self.prefixSum.append(nums[i] + self.prefixSum[-1])
        

    def sumRange(self, left: int, right: int) -> int:
        totalSum = 0
        if left == 0:
            totalSum = self.prefixSum[right]
        else:
            totalSum = self.prefixSum[right] - self.prefixSum[left-1]                 
        return totalSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)