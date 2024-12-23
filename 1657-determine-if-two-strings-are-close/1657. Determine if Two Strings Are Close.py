class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            count1[word1[i]] += 1
            count2[word2[i]] += 1

        freq = list(count2.values())

        if count1 == count2:
            return True

        if count1.keys() != count2.keys():
            return False

        for key in count1:
            if count1[key] not in freq:
                return False
            freq.remove(count1[key])

        return True
        