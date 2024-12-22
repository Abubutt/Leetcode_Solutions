class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxFreq = 0
        totalFreq = 0
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
            maxFreq = max(maxFreq, freq[num])

        for num in freq:
            if freq[num] == maxFreq:
                totalFreq += maxFreq

        return totalFreq
        