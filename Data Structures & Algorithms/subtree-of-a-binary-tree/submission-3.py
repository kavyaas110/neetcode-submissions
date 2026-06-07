# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            return self.sameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        elif root == None and subRoot == None:
            return True
        else:
            return False
    
    def sameTree(self, root1, root2):
        if root1 and root2 and (root1.val == root2.val):
            return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right,root2.right)
        elif root1 == None and root2 == None:
            return True
        else:
            return False
        