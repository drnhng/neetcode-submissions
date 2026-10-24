# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, None, None)
    def dfs(self, root:Optional[TreeNode], top: Optional[int], dir: Optional[int]):
        if not root:
            return True
        if top and dir == 0 and root.val >= top:
            return False
        if top and dir == 1 and root.val <= top:
            return False
        left = self.dfs(root.left, root.val, 0)
        right = self.dfs(root.right, root.val, 1)
        return left and right
