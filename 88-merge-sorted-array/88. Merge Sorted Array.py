class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1

        currIdx = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[currIdx] = nums1[i]
                i-=1
            else:
                nums1[currIdx] = nums2[j]
                j-=1
            
            currIdx -= 1

        while j >= 0:
            nums1[currIdx] = nums2[j]
            currIdx -= 1
            j -= 1
        
        # [2, 2]   [1]