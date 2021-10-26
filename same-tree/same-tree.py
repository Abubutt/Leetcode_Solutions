# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q) or (q is None and p):
            return False
        if p.left and q.right and p.right and q.left and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        if p.left and q.left and p.right is None and q.right is None and p.val == q.val:
            return self.isSameTree(p.left,q.left)
        if p.right and q.right and p.left is None and q.left is None and p.val == q.val:
            return self.isSameTree(p.right,q.right)
        if p.left is None and q.left is None and q.right is None and p.right is None and p.val == q.val:
            return True
        
        return False
        
                
            