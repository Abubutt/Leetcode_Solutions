class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()

                prevSmaller = -1
                if stack:
                    prevSmaller = stack[-1]
                
                nextSmaller = i

                cnt = (mid-prevSmaller) * (nextSmaller-mid) 
                ans += (cnt * arr[mid]) % ((10**9) + 7)

            
            stack.append(i)

        return ans % ((10**9) + 7)


        [3,1,2]
        []