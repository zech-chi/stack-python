# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = None
        last_node = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            root = node.right
            node.left = None
            if last_node:
                last_node.right = node
                last_node = node
            else:
                new_root = node
                last_node = node
        return new_root
