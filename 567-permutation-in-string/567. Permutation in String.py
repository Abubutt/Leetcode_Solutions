class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = defaultdict(int)
        currCount = defaultdict(int)
        size = len(s1)

        if len(s2) < size:
            return False

        for char in s1:
            countS1[char] += 1

        left = 0
        for i in range(size):
            currCount[s2[i]] += 1

        if countS1 == currCount:
            return True

        for right in range(size, len(s2)):
            currCount[s2[right]] += 1

            while right-left+1 > size:
                currCount[s2[left]] -= 1
                if currCount[s2[left]] <= 0:
                    del currCount[s2[left]]
                left += 1

            if currCount == countS1:
                return True

        return False


        
        