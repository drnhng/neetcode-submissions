# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.bot = False
        self.k = k
        self.ans = -1
        self.dfs(root)
        return self.ans
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return
        if self.bot:
            self.k -= 1
        if self.k < 0:
            return
        if self.k == 0:
            self.ans = root.val
            return
        
        left = self.dfs(root.left)
        if self.bot:
            self.k-=1
            if self.k==0:
                self.ans = root.val
        right = self.dfs(root.right)
        if not left and not right and not self.bot:
            self.bot = True
            self.k -=1
            if self.k == 0:
                self.ans = root.val
