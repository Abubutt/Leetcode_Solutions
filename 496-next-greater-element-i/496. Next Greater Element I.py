from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        queue = deque()
        nextGreater = {}
        ans = []
        
        for i in range(len(nums2)):
            while queue and nums2[i] > queue[0]:
                greaterVal = queue.popleft()
                nextGreater[greaterVal] = nums2[i]
            
            queue.appendleft(nums2[i])
            
        for num in nums1:
            if num in nextGreater:
                ans.append(nextGreater[num])
            else:
                ans.append(-1)
                
        return ans
        
        