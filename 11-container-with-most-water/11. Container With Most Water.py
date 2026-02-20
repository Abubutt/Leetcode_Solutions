class Solution:
    def maxArea(self, height: List[int]) -> int:
       left = 0
       right = len(height) - 1
       ans = 0

       while left < right:
        amount = (right - left) * min(height[left], height[right])
        ans = max(ans, amount)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

       return ans

        # [1,8,6,2,5,4,8,3,7]
        #    l             r

        