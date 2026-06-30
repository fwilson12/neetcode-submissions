# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive soln, slow for some reason

        if not root: return None

        # swap l/r
        temp = root.left
        root.left = root.right
        root.right = temp

        # call on children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # return this
        return root