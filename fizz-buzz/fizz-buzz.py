class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans=[]
        # for i in range(1,n+1):
        #     if i%3==0 and i%5==0:
        #         ans.append("FizzBuzz")
        #     elif i%3==0:
        #         ans.append("Fizz")
        #     elif i%5==0:
        #         ans.append("Buzz")
        #     else:
        #         ans.append(str(i))
        # return ans
        

        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]
        
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr
        