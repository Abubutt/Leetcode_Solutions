class Solution:
    def countArrangement(self, n: int) -> int:
        # using a recursive function we start from n and move towards 1 to ensure all elements are placed according to the condition
        #the 'used' array is used to keep track of the indices in which elements are placed
        used=[False for i in range(n+1)]
        self.res=0
        def recur_backtrack(x):
            if x==0:
                self.res+=1 #if we have placed all the elements
                return
            for i in range(1,n+1):
                if not used[i] and (x%i==0 or i%x==0): #if the index i is free and either i divides x or x divides i
                    used[i]=True
                    recur_backtrack(x-1) #Recursion for x-1 element to be placed
                    used[i]=False        #backtracking 
        recur_backtrack(n)
        return self.res
