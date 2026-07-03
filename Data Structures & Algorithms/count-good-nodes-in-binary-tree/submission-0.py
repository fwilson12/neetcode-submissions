# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.good = 0 

        # dfs helper
        def dfs(node, maxVal):
            if node is None: 
                return 

            # this node is good
            if node.val >= maxVal:
                self.good += 1
            
            # check left and right subtrees with updates maxVal
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))
        
        # kickoff, return res
        dfs(root, root.val)
        return self.good

