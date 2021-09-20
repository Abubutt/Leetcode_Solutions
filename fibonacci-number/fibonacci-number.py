class Solution:
    def fib(self, n: int) -> int:
        if n in [1,2]:
            return 1
        if n<1:
            return 0
        fib = [1,1]
        for i in range(2,n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n-1]
            