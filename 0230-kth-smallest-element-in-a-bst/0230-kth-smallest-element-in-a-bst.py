# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        element = []

        def left_subtree(node):
            if node == None:
                return
            
            left_subtree(node.left)
            element.append(node.val)
            left_subtree(node.right)

        left_subtree(root)

        if 0 < k <= len(element):
            return element[k-1]
        else:
            return None

        