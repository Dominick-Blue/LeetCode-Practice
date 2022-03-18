# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        children = [root.left, root.right]
        
        if not any(children):
            return 1
        
        min_depth = float('inf')
        
        for child in children:
            if child:
                min_depth = min(self.minDepth(child), min_depth)
        return min_depth + 1