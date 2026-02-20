class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n = len(nums1)
        m = len(nums2)

        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            partitionX = mid
            partitionY = ((n + m + 1) // 2) - partitionX

            minRightX = float('inf')
            minRightY = float('inf')
            maxLeftX = float('-inf')
            maxLeftY = float('-inf')

            if partitionX > 0:
                maxLeftX = nums1[partitionX - 1]

            if partitionX < n:
                minRightX = nums1[partitionX]

            if partitionY > 0:
                maxLeftY = nums2[partitionY - 1]

            if partitionY < m:
                minRightY = nums2[partitionY]

            if maxLeftY <= minRightX and maxLeftX <= minRightY:
                if (n + m) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                right = mid - 1
            else:
                left = mid + 1

        