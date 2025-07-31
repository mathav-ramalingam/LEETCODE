# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        element = []
        def inorder(node):
            if node == None:
                return
            
            inorder(node.left)
            element.append(node.val)
            inorder(node.right)
        
        inorder(root)

        for i in range(len(element)):
            for j in range(i+1 , len(element)):
                if element[i] + element[j] == k:
                    return True
        
        return False