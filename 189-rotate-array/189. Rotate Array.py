class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotations = k % len(nums)

        if rotations == 0:
            return

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(nums, 0, len(nums) - rotations - 1)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, rotations - 1)

        # [1,2,3,4,5,6,7]
        # [4,3,2,1,5,6,7]
        # [7,6,5,4,3,2,1]


        # [5,6,7,1,2,3,4]

        # [99, 3, -1, -100]

        # [4,3,2,1,5,6,7] # reverse from 0 to end - k
        # [7,6,5,1,2,3,4] # reverse 0 to end
        # [5,6,7,1,2,3,4] # reverse 0 to end - k

        # [-100,-1,3,99]
        # [99, 3, -1, -100]
        # [3,99, -1, 100]