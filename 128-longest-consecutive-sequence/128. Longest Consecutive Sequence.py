class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        visited = defaultdict(int)

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 1
                while num + 1 in nums_set:
                    if num in visited:
                        curr += visited[currNum]
                        break
                    
                    num += 1
                    curr += 1
                visited[num] = curr
                ans = max(ans, curr)

        return ans
        