# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs

        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        pQ = deque([p])
        qQ = deque([q])
        while pQ and qQ:
            
            pNode = pQ.popleft()
            qNode = qQ.popleft()

            if pNode.val != qNode.val: return False

            if pNode.left and qNode.left:
                pQ.append(pNode.left)
                qQ.append(qNode.left)
            # to get here they were either both null or both existed; if one exists but not the other, not the same tree
            elif pNode.left or qNode.left: return False


            if pNode.right and qNode.right:
                pQ.append(pNode.right)
                qQ.append(qNode.right)
            elif pNode.right or qNode.right: return False

        
        return True
            


