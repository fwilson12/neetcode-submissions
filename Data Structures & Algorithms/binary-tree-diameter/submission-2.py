# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs 
        
        if root is None: return 0

        # the longest path through the current node is the sum of the max length of their left and right subtrees. 
        # however, the longest path may not run through this node, so check its kids
        return max((self.maxDepth(root.left) + self.maxDepth(root.right)), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    # hello old friend
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs 
        if not root: return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))