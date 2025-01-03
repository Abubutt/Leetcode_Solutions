class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        stack_len = 0
        size = len(nums)
        for idx, num in enumerate(nums):
            while stack and stack[-1] > num and size-idx-1 >= k-stack_len:
                stack.pop()
                stack_len -= 1

            if stack_len < k:
                stack.append(num)
                stack_len += 1
            
        return stack