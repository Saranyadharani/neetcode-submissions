# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def validtree(node,low,high):
            # base case: the empty node is valid
            if not node:
                return True

            # checking whether the value bound between between the range
            if not (low<node.val<high):
                return False
            #recursively check the remaining node whether they lie in the same range
            return (validtree(node.left,low,node.val)and validtree(node.right,node.val,high))
        return validtree(root,float('-inf'),float('inf'))