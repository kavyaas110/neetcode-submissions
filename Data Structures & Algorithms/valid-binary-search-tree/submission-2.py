# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       return self.myValidChecker(root, float("-inf"), float("inf"))

    def myValidChecker(self,node, left, right):
        if not node:
            return True
        else:
            if not (node.val < right and node.val > left):
                return False
            
            return self.myValidChecker(node.left, left, node.val) and self.myValidChecker(node.right, node.val, right)
        