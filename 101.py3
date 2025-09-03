# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compareChildren(left,right):
            if(not left and not right):
                return True # Both are null, traversal done
            if((not left or not right) or left.val!=right.val):
                return False    # Mismatch
            return(compareChildren(left.right,right.left) and compareChildren(left.left,right.right))
        return compareChildren(root.left,root.right)
        
