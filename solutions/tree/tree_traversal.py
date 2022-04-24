from solutions.tree.tree_node import TreeNode


def preorder(root: TreeNode, list: list[int]) -> list[int]:
    if root is None: return list
    if root.left is not None: preorder(root.left, list)
    list.append(root.val)
    if root.right is not None: preorder(root.right, list)
