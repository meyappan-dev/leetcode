# Last updated: 5/11/2025, 8:39:05 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right))
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)