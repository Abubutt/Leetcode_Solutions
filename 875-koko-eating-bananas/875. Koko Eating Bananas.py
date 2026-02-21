class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        def check(k):
            taken = 0
            for pile in piles:
                taken += math.ceil(pile / k)
            return taken <= h

        while left <= right:
            mid = (left + right) // 2
            valid = check(mid)

            if valid:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
        