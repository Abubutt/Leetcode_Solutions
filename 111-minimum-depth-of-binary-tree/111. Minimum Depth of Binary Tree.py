# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.depth = float('inf')
        
        def dfs(node, curr):
            if not node:
                return
            
            if not node.left and not node.right:
                self.depth = min(self.depth, curr)
                
            if node.left:
                dfs(node.left, curr+1)
            
            if node.right:
                dfs(node.right, curr+1)
                
        dfs(root, 1)
        return self.depth
        