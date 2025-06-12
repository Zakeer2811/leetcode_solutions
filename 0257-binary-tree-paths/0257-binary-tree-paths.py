from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if root:
            self.searchBT(root, "", paths)
        return paths

    def searchBT(self, node: TreeNode, path: str, paths: List[str]):
        if not node.left and not node.right:
            paths.append(path + str(node.val))
        if node.left:
            self.searchBT(node.left, path + str(node.val) + "->", paths)
        if node.right:
            self.searchBT(node.right, path + str(node.val) + "->", paths)
