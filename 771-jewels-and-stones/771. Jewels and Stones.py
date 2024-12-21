class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelTypes = set(jewels)
        totalJewels = 0
        
        for stone in stones:
            if stone in jewelTypes:
                totalJewels += 1
                
        return totalJewels
        