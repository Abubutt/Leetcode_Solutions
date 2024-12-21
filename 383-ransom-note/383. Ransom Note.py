class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         countNote = defaultdict(int)
#         countMag = defaultdict(int)
        
#         for char in ransomNote:
#             countNote[char] += 1
            
#         for char in magazine:
#             countMag[char] += 1
        
#         for key in countNote:
#             if countMag[key] < countNote[key]:
#                 return False
        
#         return True
          
        countMag = defaultdict(int)
        
        for char in magazine:
            countMag[char] += 1
            
        for char in ransomNote:
            if countMag[char] <= 0:
                return False
            countMag[char] -= 1
            
        return True
            
        
