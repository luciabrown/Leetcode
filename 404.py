# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def leftLeaves(node, isLeft):
            if(not node):                           # Passed leaf
                return 0        
            if(not node.left and not node.right):   # Leaf
                if(isLeft):                         # Left leaf
                    return node.val                 # Add val
                else:                               # Right leaf
                    return 0                        # Don't add val
            return (leftLeaves(node.left,True) + leftLeaves(node.right,False))  # Explore both subtrees
        return leftLeaves(root,False)               # Start at root
