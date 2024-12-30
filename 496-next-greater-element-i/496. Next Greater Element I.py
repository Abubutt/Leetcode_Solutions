class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextElement = defaultdict(int)
        stack = []
        ans = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                nextElement[val] = nums2[i]
                
            stack.append(nums2[i])
            
        for num in nums1:
            if num in nextElement:
                ans.append(nextElement[num])
            else:
                ans.append(-1)
                
        return ans
        