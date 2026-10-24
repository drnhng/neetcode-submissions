# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.recurse(root, 0)
        return self.ans
    def recurse(self, root: Optional[TreeNode], sum: int):
        if not root:
            return 0
        sum = sum + root.val
        self.ans = max(self.ans, sum)
        left = self.recurse(root.left, sum)
        right = self.recurse(root.right, sum)
        maxSum = max(left, right)
        self.ans = max(self.ans, maxSum)
        return maxSum
