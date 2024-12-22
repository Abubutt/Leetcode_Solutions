class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        seen = set()

        for num in arr:
            freq[num] += 1

        for num in freq:
            if freq[num] in seen:
                return False
            seen.add(freq[num])
        
        return True
        