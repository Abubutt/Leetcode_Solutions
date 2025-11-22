class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp_val = {}  # value -> longest length ending at this value
        ans = 0

        for a in arr:
            prev = a - difference
            best_before = dp_val.get(prev, 0)
            dp_val[a] = best_before + 1
            ans = max(ans, dp_val[a])

        return ans
