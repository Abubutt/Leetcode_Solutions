class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()
        ans = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if (nums[i], nums[j], nums[k]) in seen:
                    j += 1
                    k -= 1
                    continue

                if (nums[i] + nums[j] + nums[k]) == 0:
                    seen.add((nums[i], nums[j], nums[k]))
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    k -= 1

        return ans         