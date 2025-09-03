# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        self.minDepth=sys.maxsize
        self.dfs(root,0)
        return self.minDepth

    def dfs(self,root,depth):
        if(not root):
            return 0
        if(not root.left and not root.right):
            self.minDepth = min(self.minDepth,depth+1)
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)
