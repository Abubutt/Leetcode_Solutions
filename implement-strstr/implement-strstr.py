class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        elif haystack == needle or needle == "":
            return 0
        else:
            return haystack.find(needle)