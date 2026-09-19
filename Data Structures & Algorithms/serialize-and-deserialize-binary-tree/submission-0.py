# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # if there is no root return null
        if not root:
            return "null"
        result=[]
        def preorder(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="null":
            return None
        values=data.split(",")
        queue=deque(values)
        def build():
            val=queue.popleft()
            if val=="null":
                return None
            node=TreeNode(int(val))
            node.left=build()
            node.right=build()
            return node
        return build()
