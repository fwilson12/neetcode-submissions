# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs helper
        def validate(node, possible):
            if node is None:
                return True
            
            # the current node is in the valid range, as are its children
            return (node.val in range(possible[0], possible[1]) 
                    and validate(node.left, [possible[0], node.val]) # left child must be an element in [running min, parent - 1]
                    and validate(node.right,[node.val + 1, possible[1]])) # right must be in [parent + 1, running max]
        
        return validate(root, [-9999, 9999])