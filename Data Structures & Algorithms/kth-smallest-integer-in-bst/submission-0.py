# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder
        # counter to come out of and if it's the same number as k, return root.val?
        res = None
        count = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal count, res
            if not node or res is not None:
                return
            
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res