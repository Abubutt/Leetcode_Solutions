class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(word1)):
            count1[word1[i]] += 1
            count2[word2[i]] += 1

        if count1 == count2:
            return True
        
        if count1.keys() != count2.keys():
            return False
        
        values = list(count2.values())
        for key in count1:
            print(values, count1[key])
            if count1[key] not in values:
                return False
            values.remove(count1[key])

        return True

        # "abbzzca". a1 b1 z0 c1
        # "babzzcz". b1 a0 z1 c1