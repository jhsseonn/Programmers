# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root.left and root.right==null:
#             return True
#         if root.left==null or root.right==null:
#             return False
#         if root.left!=null and root.right!=null:
#             return self.isSymmetric(root.left) and self.isSymmetric(root.right)
