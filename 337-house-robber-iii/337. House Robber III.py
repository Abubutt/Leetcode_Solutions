# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(node, robbed):
            if (node, robbed) in memo:
                return memo[(node, robbed)]

            if not node:
                return 0

            if robbed:
                memo[(node, robbed)] = dp(node.left, False) + dp(node.right, False)
                return memo[(node, robbed)]
            else:
                memo[(node, robbed)] =  max(node.val + dp(node.left, True) + dp(node.right, True), dp(node.left, False) + dp(node.right, False))
                return memo[(node, robbed)]

        return max(dp(root, True), dp(root, False))
        