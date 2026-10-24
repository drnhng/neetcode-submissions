# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('inf'), float('-inf'), 0)
    def check(self, root: Optional[TreeNode], leftCheck: int, rightCheck: int, prev: int):
        if not root:
            return True
        if prev == 1 and root.val > leftCheck:
            return False
        if prev == 2 and root.val < rightCheck:
            return False
        leftCheck = min(leftCheck, root.val)
        rightCheck = max(rightCheck, root.val)
        return self.check(root.left, leftCheck, rightCheck, 1) and self.check(root.right, leftCheck, rightCheck, 2)