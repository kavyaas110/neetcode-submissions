# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if self.isLeaf(p) and self.isLeaf(q):
                return p.val == q.val
            elif (not self.isLeaf(p)) and (not self.isLeaf(q)):
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        elif (not p) and (not q):
            return True
        else:
            return False

    
    def isLeaf(self, n: TreeNode):
        if n.left == None and n.right == None:
            return True
        else:
            return False
        