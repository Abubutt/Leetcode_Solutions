class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxOccurence = len(nums)/2
        total = Counter(nums)
        for key,value in total.items():
            if value > maxOccurence:
                return key