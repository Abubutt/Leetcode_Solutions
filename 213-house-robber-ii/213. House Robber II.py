class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dp(i, arr, memo):
            if i in memo:
                return memo[i]

            if i == 0:
                return arr[i]

            if i < 0:
                return 0

            pick = arr[i] + dp(i-2, arr, memo)
            notPick = dp(i-1, arr, memo)

            memo[i] = max(pick, notPick)
            return memo[i]

        nums1 = nums[:-1]
        nums2 = nums[1:]

        return max(dp(len(nums1) - 1, nums1, {}), dp(len(nums2) - 1, nums2, {}))
        