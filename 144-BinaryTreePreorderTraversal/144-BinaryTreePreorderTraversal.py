# Last updated: 3/28/2025, 9:58:57 AM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.preOrder(root,arr)
        return arr
    
    def preOrder(self,root,arr):
        if root is None:
            return
        
        arr.append(root.val)
        self.preOrder(root.left,arr)
        self.preOrder(root.right,arr)