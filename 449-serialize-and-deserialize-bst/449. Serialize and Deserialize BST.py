# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        preorder = []
        inorder = []

        def pre(root):
            if not root:
                return None

            preorder.append(str(root.val))
            pre(root.left)
            pre(root.right)

        def inord(root):
            if not root:
                return None

            inord(root.left)
            inorder.append(str(root.val))
            inord(root.right)

        pre(root)
        inord(root)

        return "#".join(preorder) + ":" + "#".join(inorder)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder, inorder = data.split(":")
        preorder = preorder.split("#")
        inorder = inorder.split("#")

        if preorder[0] == '':
            return None

        def constructTree(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = preorder[0]
            node = TreeNode(int(root))
            mid = inorder.index(root)

            node.left = constructTree(preorder[1:mid+1], inorder[:mid])
            node.right = constructTree(preorder[mid + 1:], inorder[mid + 1:])

            return node

        return constructTree(preorder, inorder)
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans