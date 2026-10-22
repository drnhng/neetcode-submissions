# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        q.append(root)
        ans = []

        while q:
            size = len(q)
            curr = -1
            for i in range(size):
                top = q.popleft()
                curr = top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            ans.append(curr)
        return ans