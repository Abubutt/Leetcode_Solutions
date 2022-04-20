class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 0(nlogn)
        # numDict = defaultdict(int)
        # ans = []
        # for num in nums:
        #     if num in numDict:
        #         numDict[num] += 1
        #     else:
        #         numDict[num] = 0
        # numDict = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
        # print(numDict)
        # for key,val in numDict:
        #     if k == 0:
        #         break
        #     else:
        #         ans.append(key)
        #     k-=1
        # return ans
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key,val in count.items():
            freq[val].append(key)
            
        ans = []
        
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans