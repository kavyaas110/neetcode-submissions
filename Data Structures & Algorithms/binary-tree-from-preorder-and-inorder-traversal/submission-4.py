# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_index_dict = {val:index for index,val in enumerate(inorder)}
        return self.helper(preorder, inorder, val_index_dict, 0, len(inorder))
        
            
    def helper(self, preoder, inorder, val_index_dict, start, end):
        # print(inorder[start:end], preorder)
        if not preorder:
            return None

        val = preorder[0]
        val_index = val_index_dict[val]
        if val_index >= start and val_index < end:
            preorder.pop(0)
            node = TreeNode(val)
            node.left = self.helper(preorder,inorder, val_index_dict, start, val_index)
            node.right = self.helper(preorder,inorder, val_index_dict, val_index+1, end)        
            return node
        else:
            return None
        