# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # alternative Solution

        self.res = 0

        def dfs(curr):
            if not curr: return 0

            # postorder 
            left = dfs(curr.left)
            right = dfs(curr.right)

            # the current diameter is the sum of the max length of the left and right subtree
            self.res = max(self.res, left + right)
            # this is for the height of the current node (how we calculate l/r) 
            return 1 + max(left, right)

        # kickoff
        dfs(root)
        return self.res
