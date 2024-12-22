class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mappingP = {}
        mappingS = {}

        t = s.split(" ")

        if len(pattern) != len(t):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mappingP:
                mappingP[pattern[i]] = t[i]
            if t[i] not in mappingS:
                mappingS[t[i]] = pattern[i]
            if mappingP[pattern[i]] != t[i] or mappingS[t[i]] != pattern[i]:
                return False

        return True
        