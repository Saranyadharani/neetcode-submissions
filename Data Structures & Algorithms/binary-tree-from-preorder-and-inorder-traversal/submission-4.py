# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # using hashmap in the inorder 
        inorder_map={ val:i for i,val in enumerate (inorder)}
        def build(pre_start,pre_end,in_start,in_end):
            if pre_start>pre_end or in_start>in_end:
                return None
            # take the root 
            root_val=preorder[pre_start]
            root=TreeNode(root_val)
            #find the mid
            mid=inorder_map[root_val]
            left_size=mid-in_start
            root.left=build(pre_start+1,pre_start+left_size,in_start,mid-1)
            root.right=build(pre_start+left_size+1,pre_end,mid+1,in_end)
            return root
        return build(0,len(preorder)-1,0,len(inorder)-1)