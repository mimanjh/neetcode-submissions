# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # get the index of inorder's root from preorder's first value
        firstVal = preorder[0]
        index = inorder.index(firstVal)
        root = TreeNode(firstVal)
        # from the preorder, left would be the left tree, right would be the right tree
        # from the inorder, same number of lefts will be left, and right vice versa
        root.left = self.buildTree(preorder[1: index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1: ])

        return root

