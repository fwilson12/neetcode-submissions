# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs variant
        
        bfs = deque()

        if not root: return None

        bfs.append(root)

        while bfs:

            node = bfs.popleft()

            if node.left:
                bfs.append(node.left)

            if node.right:
                bfs.append(node.right)

            node.left, node.right = node.right, node.left
        
        return root
