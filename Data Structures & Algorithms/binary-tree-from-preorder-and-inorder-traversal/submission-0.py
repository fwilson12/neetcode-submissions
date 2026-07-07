# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # done when there are no nodes left (obviously)
        if not (preorder or inorder): return None

        # get value of the current root node, used as a key to figure out which values are to the left/right of the root via the inorder trav
        rootVal = preorder[0]
        root = TreeNode(rootVal) # init root
        mid = inorder.index(rootVal) # where our current root is in the inorder trav

        # assign left subtree to be the root of the next elem in preorder (if it exists) and throw in the values that actually belong there (via inorder split)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # same with right
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
        return root 