# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # an empty node is balanced
        if root is None: return True

        # height helper
        def dfs(node):

            if not node: return 0

            return 1 + max(dfs(node.left), dfs(node.right))
        
        # left and right heights   
        left, right = dfs(root.left), dfs(root.right)

        # current tree is balanced, and its subtrees are too
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)