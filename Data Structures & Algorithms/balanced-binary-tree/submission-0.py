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

        self.balanced = True

        # height helper
        def dfs(node):

            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # check as we traverse
            if abs(left - right) > 1: 
                self.balanced = False
            return 1 + max(left, right)
        
        # kickoff
        dfs(root)

        # current tree is balanced, and its subtrees are too
        return self.balanced