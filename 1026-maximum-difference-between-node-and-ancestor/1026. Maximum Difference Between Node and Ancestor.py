# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        minVal = float('inf')
        maxVal = float('-inf')
        
        def dfs(root, minVal, maxVal):
            if not root:
                return 0
            
            minVal = min(root.val, minVal)
            maxVal = max(root.val, maxVal)
            
            left = dfs(root.left, minVal, maxVal)
            right = dfs(root.right, minVal, maxVal)
            
            return max(abs(maxVal - minVal), left, right)
        
        return dfs(root, minVal, maxVal)
            
            
        