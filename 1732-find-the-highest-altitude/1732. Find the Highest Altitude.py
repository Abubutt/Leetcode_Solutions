class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = currGain = 0

        for num in gain:
            currGain += num
            ans = max(ans, currGain)

        return ans