# Last updated: 5/11/2025, 2:00:32 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        count = 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        return count