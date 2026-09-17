# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check whether both tree are empty if yes return True
        if not p and not q:
            return True
        # if one tree is there and another tree is empty return False
        if not p or not q:
            return False
        
        # checking the nodes values of the 2 trees
        if p.val!=q.val:
            return False
        return ((self.isSameTree(p.left,q.left))and (self.isSameTree(p.right,q.right)))