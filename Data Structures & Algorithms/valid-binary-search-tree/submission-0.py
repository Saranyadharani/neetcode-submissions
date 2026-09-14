# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        # left child node < root node < right child node
        def validate(node,low,high):
            if not node:
                return True
            #check the node is within the range
            if not (low<node.val<high):
                return False
            return (validate(node.left,low,node.val)and validate (node.right,node.val,high))
        return validate(root,float('-inf'),float('inf'))