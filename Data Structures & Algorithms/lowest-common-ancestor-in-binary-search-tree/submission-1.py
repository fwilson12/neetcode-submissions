# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # global lowest. updates as we go deeper
        self.lowest = root

        # dfs helper to find lowest CA
        def dfs(root, p, q):
            
            # bottom of tree
            if root is None: return 

            # root is ancestor of p and q, so update lowest since we can't go higher up the tree from here
            if self.hasAncestor(root, p) and self.hasAncestor(root, q): self.lowest = root

            # check children
            dfs(root.left, p, q)
            dfs(root.right, p, q)

        # kickoff + return res
        dfs(root, p, q)
        return self.lowest

    # does node have an ancestor root?
    def hasAncestor(self, root, node):
        
        if root is None: return False

        if root.val == node.val: return True

        return self.hasAncestor(root.left, node) or self.hasAncestor(root.right, node)