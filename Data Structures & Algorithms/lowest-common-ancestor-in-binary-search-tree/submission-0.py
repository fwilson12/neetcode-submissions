# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.lowest = root

        def dfs(root, p, q):
            
            if root is None: return 

            if self.hasAncestor(root, p) and self.hasAncestor(root, q): self.lowest = root

            dfs(root.left, p, q)
            dfs(root.right, p, q)

        dfs(root, p, q)
        return self.lowest

    # does node have an ancestor root
    def hasAncestor(self, root, node):
        
        if root is None: return False

        if root.val == node.val: return True

        return self.hasAncestor(root.left, node) or self.hasAncestor(root.right, node)