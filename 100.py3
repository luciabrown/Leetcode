# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q):    # Both are null - reached end
            return True
        if((not p or not q) or (p.val!=q.val)): # One is null and other is not OR they have diff vals
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
