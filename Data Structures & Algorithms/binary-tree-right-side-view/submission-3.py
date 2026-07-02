# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
# optimal Solution
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # bfs, but only append the last node popped 

        if root is None: return []

        res = []
        q = deque([root])

        while q:
            
            lastNode = None
            # parse all nodes from this level
            for i in range(len(q)):
                node = q.popleft()
                lastNode = node

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res.append(lastNode.val)
            

        return res