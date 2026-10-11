class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        [0,0,0,0,0,1,1,2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j+=1
                    continue
                if (nums[i] + nums[j] + nums[k]) == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # while j < k and nums[j] == nums[j - 1]:
                    #     j += 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    k -= 1

        return ans         

        # [-4, -1, -1, 0, 1, 2]