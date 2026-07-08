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

            # ok. so we update the res as if the current node is the connector or top of the path. 
            # This is why we can add its value to the left and right values. However, we still want to 
            # contribute information to the parent, which may be already branching out to the current node's sibling. 
            # This would mean the current node would appear twice in the path. So, we must return a uni directional path 
            # from the current node to the parent to avoid forking.
            maxPathThroughNode = max(0, left, right) + node.val
            
            # update res as if this node is the top
            self.res = max(self.res, max(0, left) + max(0, right) + node.val)

            return maxPathThroughNode

        dfs(root)
        return self.res