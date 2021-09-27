class Solution:
    def reverse(self, x: int) -> int:
        num = x
        if num == 0:
            return num
        if x<0:
            num *=-1
        
        ans = ""
        while num >= 1:
            ans+=str(num%10)
            num = num//10
        
        if int(ans) > 2**31 - 1 or int(ans) < -2**31:
            return 0
        if x < 0:
            return int(ans)*-1
        else:
            return int(ans)
        