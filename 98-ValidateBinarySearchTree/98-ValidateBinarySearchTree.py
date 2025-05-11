# Last updated: 5/11/2025, 1:47:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum,maximum = float('-inf'), float('inf')
        return self.checkForBST(root,minimum,maximum)
    
    def checkForBST(self,root,minimum,maximum):
        if root == None:
            return True
        if (minimum < root.val < maximum):
            return self.checkForBST(root.left,minimum,root.val) and self.checkForBST(root.right,root.val,maximum)
        else:
            return False