# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # optimal Solution

        self.nodes = []
        self.count = 0

        def inorder(root):

            # don't add if we've already hit the count
            if root is None or self.count == k: return 

            # process left values first (inorder traversal of a BST yields strictly increasing seq)
            inorder(root.left)
            if self.count == k: return # may have hit the count here, if so return before we add the current root

            # process this guy, update res and count
            self.nodes.append(root.val)
            self.count += 1
            
            # process right subtree
            inorder(root.right)
        
        # kickoff, then return the last element in res (kth smallest, kth element visited in an inorder trav)
        inorder(root)
        return self.nodes[-1] if self.nodes else -1

