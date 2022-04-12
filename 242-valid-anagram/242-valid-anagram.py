class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time 0(n) space 0(s + t)
#         if len(s) != len(t):
#             return False
#         s_dict = {}
#         t_dict = {}
        
#         for i in range(len(s)):
#             s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
#             t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
            
#         for key in t:
#             if t_dict[key] != s_dict.get(key, 0):
#                 return False
#         return True

        # time 0(nlogn) space 0(1)
        return sorted(s) == sorted(t)