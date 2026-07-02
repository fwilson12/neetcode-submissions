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
            lastNode = len(q) - 1
            # collect all nodes from this level
            for i in range(len(q)):
                node = q.popleft()
                # just want the value of the right-most node on this level
                if i == lastNode:
                    res.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            

        return res