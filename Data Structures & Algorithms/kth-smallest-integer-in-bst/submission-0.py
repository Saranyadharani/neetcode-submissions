# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # initialize count and result
        self.count=0
        self.result=None
        #add a inorder function
        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            self.count+=1
            if self.count==k:
                self.result=node.val
                return
            inorder(node.right)
        inorder(root)
        return self.result