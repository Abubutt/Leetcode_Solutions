class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappingS = {}
        mappingT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in mappingS:
                mappingS[s[i]] = t[i]
            if t[i] not in mappingT:
                mappingT[t[i]] = s[i]
            if mappingS[s[i]] != t[i] or mappingT[t[i]] != s[i]:
                return False

        return True
        