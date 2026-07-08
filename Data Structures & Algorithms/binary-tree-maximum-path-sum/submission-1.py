# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.res = root.val

        # dfs helper
        def dfs(node):

            if node is None: return 0

            # get children max paths first  
            left = dfs(node.left)
            right = dfs(node.right)

            # the 
            maxPathThroughNode = max(0, left, right) + node.val
            
            
            self.res = max(self.res, max(0, left) + max(0, right) + node.val)

            return maxPathThroughNode

        dfs(root)
        return self.res