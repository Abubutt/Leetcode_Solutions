class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            leftVal = nums[left]
            rightVal = nums[right]

            if midVal == target:
                return mid

            if leftVal <= midVal <= rightVal:
                if midVal < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif leftVal <= midVal and midVal > rightVal:
                if leftVal <= target <= midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if midVal <= target <= rightVal:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        