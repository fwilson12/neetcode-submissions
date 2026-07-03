# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.heap = []
        def dfs(node):

            if node is None: return

            heapq.heappush(self.heap, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        res = -1
        for i in range(k):
            res = heapq.heappop(self.heap)
        return res
