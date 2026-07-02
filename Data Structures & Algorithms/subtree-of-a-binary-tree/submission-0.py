# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # both are None
        if not (root or subRoot): return True
        # one is none, not a subtree
        if not root or not subRoot: return False

        # helper
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False

            # the two curr vals are equal, and so are their subtrees
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(q.right, p.right)

        # check current node and its children
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



        