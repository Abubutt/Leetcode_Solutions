class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start < end:
            while s[start].isalnum() == False:
                if start >= end:
                    return True
                start+=1
            while s[end].isalnum() == False:
                if end < 0: 
                    return False
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            
            start+=1
            end -= 1
        return True