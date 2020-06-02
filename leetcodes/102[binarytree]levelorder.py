# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = []
        out = []
        q.append(root)
        while q:
            size = len(q)
            current_level = []
            for _ in range(0,size):
                ele = q.pop(0)
                current_level.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            out.append(current_level)
        return out
        