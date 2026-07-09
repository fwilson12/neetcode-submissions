# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "NULL"

        return f"{root.val} | {self.serialize(root.left)} | {self.serialize(root.right)}"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        # root node is at the top of the stack
        treeVals = data.split(" | ")
        treeVals.reverse()

        # actual func
        def build():
            val = treeVals.pop()

            if val == "NULL":
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        # kickoff
        return build()



















