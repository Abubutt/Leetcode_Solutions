class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freqList = [[] for i in range(len(nums) + 1)]

        for key, val in count.items():
            freqList[val].append(key)

        for i in range(len(freqList) - 1, -1, -1):
            for val in freqList[i]:
                ans.append(val)
                k-=1

                if k == 0:
                    break
            
            if k == 0:
                break

        return ans