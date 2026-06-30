# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iter dfs

        if root is None: return 0

        nodeStack = [(root, 1)] # node, depth
        deepest = 1
        while nodeStack:
            node, depth = nodeStack.pop()

            if node.left:
                nodeStack.append((node.left, depth + 1)) 
            
            if node.right:
                nodeStack.append((node.right, depth + 1))

            deepest = max(deepest, depth)

        return deepest

