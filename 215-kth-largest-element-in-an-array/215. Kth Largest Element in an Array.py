class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], -1*i))

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)[0]
        