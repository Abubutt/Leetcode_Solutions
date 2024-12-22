class Solution:
    def frequencySort(self, s: str) -> str:
        count = [set() for i in range(len(s) + 1)]
        freq = defaultdict(int)
        ans = []

        for char in s:
            freq[char] += 1

        for char in s:
            count[freq[char]].add(char)

        print(freq)
        print(count)
        
        for i in range(len(count) - 1, -1, -1):
            for char in count[i]:
                ans.extend([char]*i)
        
        return "".join(ans)


        