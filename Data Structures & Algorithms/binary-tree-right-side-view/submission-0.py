# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs, but only append the last node popped 

        if root is None: return []

        res = []
        q = deque([root])

        while q:
            
            # collect all nodes from this level
            levelNodes = []
            while q: 
                levelNodes.append(q.popleft())

            # add children to q in order
            for node in levelNodes:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            # just want the values of the nodes in each res entry
            res.append(levelNodes[-1].val)

        return res