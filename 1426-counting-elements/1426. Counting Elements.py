class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique = set(arr)
        total = 0
        
        for num in arr:
            if num+1 in unique:
                total+=1
                
        return total
        