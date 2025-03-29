# Last updated: 3/29/2025, 12:52:14 PM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.postOrder(root,arr)
        return arr

    def postOrder(self, root, arr):
        if root is None:
            return
        
        self.postOrder(root.left,arr)
        self.postOrder(root.right,arr)
        arr.append(root.val)
