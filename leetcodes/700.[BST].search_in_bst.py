# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        elif val < root.val:
            return self.searchBST(root.left,val)
        else:
            return None

s = Solution()
print(s.searchBST([4,2,7,1,3],2))