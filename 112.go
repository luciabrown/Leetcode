// 112. Path Sum

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil{
        return false
    }
    // If leaf, check if target sum was reached
    if isLeaf(root){
        return targetSum == root.Val
    }
    // Expand left subtree
    if root.Left != nil{
        if hasPathSum(root.Left, targetSum-root.Val){
            return true
        }
    }
    // Expand right subtree
    if root.Right != nil{
        if hasPathSum(root.Right, targetSum-root.Val){
            return true
        }
    }
    return false
}

// Helper function to check if a node is a leaf
func isLeaf(possibleLeaf *TreeNode) bool{
    if possibleLeaf.Left == nil && possibleLeaf.Right == nil{
        return true
    }
    return false
}
