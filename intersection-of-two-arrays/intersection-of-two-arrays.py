class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set()
        ans = []
        big = 0
        small = 0
        if nums1 < nums2:
            big = nums2
            small = nums1
        else:
            big = nums1
            small = nums2
        for i in big:
            if i not in numSet:
                numSet.add(i)
        
        for i in small:
            if i in numSet and i not in ans:
                ans.append(i)
        return ans
            