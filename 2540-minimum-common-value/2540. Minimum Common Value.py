class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        ans = -1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                ans = nums1[i]
                break
        
        return ans
        