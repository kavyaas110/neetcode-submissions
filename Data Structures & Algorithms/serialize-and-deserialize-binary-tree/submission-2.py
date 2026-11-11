# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = ""
        def helper(node, out):
            if node:
                out += str(node.val) + " "
                out += helper(node.left, "")
                out += helper(node.right, "")
            else:
                out += "N "
            
            return out
        
        # print(out)
        return helper(root, out)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(" ")
        self.i = 0
        def helper():
            # print(data)
            val = vals[self.i]
            if val == 'N':
                self.i += 1
                return None
            else:
                val = int(val)
                self.i += 1
                node = TreeNode(val = val)
                node.left = helper()
                node.right = helper()
                return node
        root = helper()
        print(root)
        return root
