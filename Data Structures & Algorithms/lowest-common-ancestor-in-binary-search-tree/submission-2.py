# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # better soln

        curr = root
        # guranteed to find LCA
        while True:
            
            # if both values are greater than curr, LCA is in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if both values are less than curr, LCA is in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # either p and q are split by curr, or curr IS p or q; in which case curr is the LCA
            else:
                return curr