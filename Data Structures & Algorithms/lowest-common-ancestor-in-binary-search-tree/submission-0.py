# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.left:
            node_a_anc = self.check_ancestor(root.left,p)
            node_b_anc = self.check_ancestor(root.left,q)
            if node_a_anc and node_b_anc:
                return self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            node_a_anc = self.check_ancestor(root.right,p)
            node_b_anc = self.check_ancestor(root.right,q)
            if node_a_anc and node_b_anc:
                return self.lowestCommonAncestor(root.right, p, q)

        return root

    def check_ancestor(self, root, node):
        if root.val == node.val:
            return True
        else:
            res = False
            if root.left:
                res = self.check_ancestor(root.left, node)
            if root.right and not res:
                res = self.check_ancestor(root.right, node)
            return res
        