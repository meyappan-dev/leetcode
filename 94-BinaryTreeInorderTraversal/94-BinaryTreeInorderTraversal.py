# Last updated: 3/28/2025, 9:54:41 AM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.in_order(root, arr)
        return arr

    def in_order(self, root, arr):
        if root is None:
            return
        self.in_order(root.left,arr)
        arr.append(root.val)
        self.in_order(root.right,arr)