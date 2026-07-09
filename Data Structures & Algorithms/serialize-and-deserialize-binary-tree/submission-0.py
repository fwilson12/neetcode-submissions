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
        
        # actual func
        def fillTree(treeVals, direction, parent):
            
            val = treeVals.pop()
            if val == "NULL": return

            newNode = TreeNode(int(val))

            if direction == "L":                           
                parent.left = newNode
                fillTree(treeVals, "L", newNode)
                fillTree(treeVals, "R", newNode)
            
            else:                
                parent.right = newNode
                fillTree(treeVals, "L", newNode)
                fillTree(treeVals, "R", newNode)
        
        
        # root node is at the top of the stack
        treeVals = data.split(" | ")
        treeVals.reverse()
        if not treeVals or treeVals[-1] == "NULL": return None

        root = TreeNode(int(treeVals.pop()))
        fillTree(treeVals, "L", root)
        fillTree(treeVals, "R", root)
        return root



















