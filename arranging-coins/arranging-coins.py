class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        num = n
        for i in range(1, n+1):
            if num-i >= 0:
                count +=1
                num-=i
            else:
                break
        return count
      
        