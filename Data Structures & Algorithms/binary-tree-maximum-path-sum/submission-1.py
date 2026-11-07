# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:  
        _, ans = self.helper(root, float('-inf'))
        return ans

    def helper(self, node, res):
        # base case
        if not node.left and not node.right:
            if node.val > res:
                res = node.val
            return node.val, res

        # calculate left subtree value without the split
        if node.left:
            left_unsplit_val, res = self.helper(node.left, res)
        else:
            left_unsplit_val = 0

        # calculate right subtree value without the split
        if node.right:
            right_unsplit_val, res = self.helper(node.right, res)
        else:
            right_unsplit_val = 0

        # calculate the value if we split this node and update the res
        split_val = node.val + left_unsplit_val + right_unsplit_val
        if split_val > res:
            res = split_val

        # return the value if we didn't split and res
        max_side = max(left_unsplit_val, right_unsplit_val)
        if max_side > 0:
            unsplit_val = node.val + max_side
        else:
            unsplit_val = node.val
        if unsplit_val > res:
            res = unsplit_val
        return  unsplit_val, res    