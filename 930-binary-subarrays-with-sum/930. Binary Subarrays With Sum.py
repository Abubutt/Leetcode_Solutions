class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # total = currSum = 0
        # count = defaultdict(int)
        # count[0] = 1

        # for num in nums:
        #     currSum += num
        #     if currSum-goal in count:
        #         total += count[currSum-goal]
        #     count[currSum] += 1

        def slidingWindow(target):
            if target < 0:
                return 0
            count = 0
            currSum = 0
            left = 0

            for right in range(len(nums)):
                currSum += nums[right]

                while currSum > target:
                    currSum -= nums[left]
                    left += 1
                
                count += (right-left+1)
            print(count)
            return count

        total = slidingWindow(goal) - slidingWindow(goal - 1)

        return total


        