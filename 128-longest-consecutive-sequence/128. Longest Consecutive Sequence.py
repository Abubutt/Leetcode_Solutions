class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        visited = defaultdict(int)
        ans = 0

        for num in unique:
            curr = 1
            currNum = num - 1
            while currNum in unique:
                if currNum in visited:
                    curr += visited[currNum]
                    break
                else:
                    curr += 1
                    currNum -= 1
            visited[num] = curr
            ans = max(ans, curr)
        
        return ans

        