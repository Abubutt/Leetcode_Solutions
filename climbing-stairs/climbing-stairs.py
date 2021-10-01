class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1,2]
        if n<2:
            return ans[0]
        for i in range(2,n):
            ans.append(ans[i-1] + ans[i-2])
        return ans[-1]