class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        luckyNum = -1

        for num in arr:
            freq[num] += 1

        for num in arr:
            if num == freq[num]:
                luckyNum = max(luckyNum, num)

        return luckyNum
        