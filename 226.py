# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def swapChildren(node):
            if(node): 
                swapChildren(node.left)
                swapChildren(node.right)
                temp=node.left
                node.left=node.right
                node.right=temp 
                return node
        return swapChildren(root)   
