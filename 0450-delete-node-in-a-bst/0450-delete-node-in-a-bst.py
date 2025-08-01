# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            if root.left:
                root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            if root.right:
                root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            min_ele = self.find_min(root.right)
            root.val = min_ele
            root.right = self.deleteNode(root.right,min_ele)

        
        return root



    def find_min(self,node):
        if not node.left:
            return node.val    
        return self.find_min(node.left)