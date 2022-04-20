class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        ans = []
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 0
        numDict = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
        
        for key,val in numDict:
            if k == 0:
                break
            else:
                ans.append(key)
            k-=1
        return ans