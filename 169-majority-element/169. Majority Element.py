class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # cts = Counter(nums)

        # for k, ct in cts.items():
        #     if ct > len(nums) // 2:
        #         return k

        if len(nums) == 1:
            return nums[0]

        nums.sort()
        ct = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ct += 1
            else:
                ct = 1

            if ct > len(nums) // 2:
                return nums[i]
        
        # [2,3,3]