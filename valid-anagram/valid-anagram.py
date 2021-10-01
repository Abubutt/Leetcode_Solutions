import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = collections.Counter(t)
        second = collections.Counter(s)
        
        for i in s:
            if first[i] != second[i]:
                return False
        return True
        
                
        