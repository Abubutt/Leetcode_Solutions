class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    ans.append(i)
                    nums1.remove(i)
        else:
            for j in nums1:
                if j in nums2:
                    ans.append(j)
                    nums2.remove(j)
        return ans
                    
                