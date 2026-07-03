# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs helper
        def dfs(node, maxVal):
            if node is None: 
                return 0

            # this node is good
            res = 1 if node.val >= maxVal else 0
            
            # check left and right subtrees with updates maxVal
            return res + dfs(node.left, max(maxVal, node.val)) + dfs(node.right, max(maxVal, node.val))
        
        # kickoff
        return dfs(root, root.val)

