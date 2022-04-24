from solutions.tree import invert_binary_tree
from solutions.tree.tree_node import TreeNode
from solutions.tree.tree_traversal import preorder


def test_happy_path():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    list = []
    preorder(invert_binary_tree.invertTree(root), list)
    assert list == [9, 7, 6, 4, 3, 2, 1]
