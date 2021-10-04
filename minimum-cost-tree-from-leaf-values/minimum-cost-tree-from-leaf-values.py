class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans=0
        while len(arr)>1:
            min_idx=arr.index(min(arr))
            if min_idx>0 and min_idx<len(arr)-1:
                ans+=min(arr[min_idx-1],arr[min_idx+1])*arr[min_idx]
            else:
                if min_idx==0:
                    ans+=arr[min_idx]*arr[min_idx+1]
                else:
                    ans+=arr[min_idx]*arr[min_idx-1]
            arr.pop(min_idx)
        return ans