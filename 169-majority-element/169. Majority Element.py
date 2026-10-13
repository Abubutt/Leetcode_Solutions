class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # cts = Counter(nums)

        # for k, ct in cts.items():
        #     if ct > len(nums) // 2:
        #         return k

        # if len(nums) == 1:
        #     return nums[0]

        # nums.sort()
        # ct = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         ct += 1
        #     else:
        #         ct = 1

        #     if ct > len(nums) // 2:
        #         return nums[i]

        ct = 0
        ans = nums[0]

        for num in nums:
            if ct == 0:
                ans = num
            
            ct += 1 if num == ans else -1

        return ans


        
        # [2,3,3]