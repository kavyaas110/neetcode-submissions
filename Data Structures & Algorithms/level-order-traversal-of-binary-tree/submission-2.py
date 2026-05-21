# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            Q = [[root]]
            ans = [[root.val]]
            h = 1
            while Q:
                level = Q.pop(0)
                next_level = []
                values = []
                for node in level:
                    if node.left:
                        values.append(node.left.val)
                        next_level.append(node.left)
                    if node.right:
                        values.append(node.right.val)
                        next_level.append(node.right)
                if next_level != []:
                    Q.append(next_level)
                    ans.append(values)
            return ans
        else:
            return []