# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional

from solutions.tree.tree_node import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None: return root
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
