# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # for below binary tree

    """ 4
       / \
      2   7
     / \ / \
    1  3 6  9     invertTree(4)= swap(2,7)=left=7,right=2
                   invertTree(7)=swap(6,9)=left=9,right=6
                   invertTree(2)=swap(1,3)=left=3,right=1

    """