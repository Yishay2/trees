class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Function 1: Inverse Tree
# Write a function `inverse_tree(root)` that receives the root of a binary tree
# and makes the tree a mirror image of itself.
# Example:
# Input Tree:
#       1
#      / \
#     2   3
#
# Output Tree:
#       1
#      / \
#     3   2

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(3), TreeNode(2))


def inverse_tree(root):
    if root is None:
        return

    inverse_tree(root.right)
    inverse_tree(root.left)
    root.left, root.right = root.right, root.left


# Function 2: Boolean Mirror Trees
# Write a function `are_mirror_trees(root1, root2)` that receives two tree roots
# and returns `True` if the trees are mirror images of each other,
# and `False` otherwise.
# Example:
# Tree 1:
#       1
#      / \
#     2   3
#
# Tree 2:
#       1
#      / \
#     3   2
# Output: True


def are_mirror_trees(root1, root2):
    if root1 is None and root2 is None:
        return True

    return root1.key == root2.key and are_mirror_trees(root1.right, root2.left) and are_mirror_trees(root1.left, root2.right)


# Function 3: Longest Zigzag Path
# Write a function `longest_zigzag(root)` that receives the root of a binary tree
# and returns a list of keys along the longest zigzag path.
# A "zigzag" occurs when the path alternates directions (left -> right -> left or right -> left -> right).
# The alternations do not have to be in consecutive levels of the tree to be considered part of a zigzag.
# Example:
# Tree:
#         1
#        / \
#       2   3
#      / \    \
#     0   4     5
#        /     / \
#       6     12  7
#                 /
#                8
#               / \
#              6   9
#                   \
#                   17
#                   /
#                  10

# Longest Zigzag Path: [3, 5, 7, 8, 9, 17, 10]


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# יצירת העץ
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

tree.left.left = Node(0)
tree.left.right = Node(4)
tree.left.right.left = Node(6)

tree.right.right = Node(5)
tree.right.right.left = Node(12)
tree.right.right.right = Node(7)

tree.right.right.right.left = Node(8)
tree.right.right.right.left.left = Node(6)
tree.right.right.right.left.right = Node(9)
tree.right.right.right.left.right.right = Node(17)
tree.right.right.right.left.right.right.left = Node(10)


def longest_zigzag(root):
    if root is None:
        return []
    l_counter, l_zigzags = _longest_zigzag(root.left, "left", 0)
    r_counter, r_zigzags = _longest_zigzag(root.right, "right", 0)
    res = (l_zigzags if l_counter > r_counter else r_zigzags) + [root.key]
    return res[::-1]


def _longest_zigzag(root, direction, counter_zigzags):
    if root is None:
        return counter_zigzags, []
    l_counter, l_zigzags = _longest_zigzag(root.left, "left", counter_zigzags + int(direction != "left"))
    r_counter, r_zigzags = _longest_zigzag(root.right, "right", counter_zigzags + int(direction != "right"))

    if r_counter > l_counter:
        return r_counter, r_zigzags + [root.key]
    return l_counter, l_zigzags + [root.key]


# Function 4: Lowest Common Ancestor
# Write a function `lowest_common_ancestor(root, node1, node2)` that receives the root of a binary tree and two nodes.
# It should return the lowest common ancestor (LCA) of the two nodes.
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
#      / \
#     8   6
#        / \
#       7   10

# LCA of 8 and 10: 5
# LCA of 6 and 4: 2
# LCA of 7 and 3: 1
#
def lowest_common_ancestor(root, node1, node2):
    if root is None:
        return

    path_node1 = _lowest_common_ancestor(root, node1)
    path_node2 = _lowest_common_ancestor(root, node2)


    # implement the logic to find the lowest common ancestor


def _lowest_common_ancestor(root, node):
    if root is None:
        return []

    if node == root.key: return [root]
    left_path = _lowest_common_ancestor(root.left, node)
    right_path = _lowest_common_ancestor(root.right, node)

    res = (left_path if left_path else right_path) + [root]
    return res


pathh = _lowest_common_ancestor(tree, 12)
print([key.key for key in pathh])

# Function 5: Print Tree by Rows
# Write a function `print_tree_by_rows(root)` that prints the tree level by level using a breadth-first search (BFS).
# Example:
# Tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#
# Output:
# 1
# 2 3
# 4 5 6

def print_tree_by_rows(root):
    pass


# Instructions for Writing Tests
# Write test cases for each of the above functions. For each test:
# - Provide an example input (tree or trees for comparison).
# - Include the expected output based on the provided examples.
# - Ensure that your tests cover various edge cases, such as empty trees, single-node trees, or trees with specific structures.
# You can use helper functions to build binary trees for testing.


# Recommendation:
# To visualize binary trees, you can use the `graphviz` library. It allows you to create graphical representations of trees
# and save them as image files. This can be especially useful for debugging and understanding tree structures.
# Example:
# 1. Install Graphviz:
#    pip install graphviz
# 2. Use the following function to visualize a binary tree:

from graphviz import Digraph

def visualize_tree(root, filename="tree"):
    def add_nodes_edges(node, dot=None):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(node.right, dot)

    dot = Digraph()
    add_nodes_edges(root, dot)
    dot.render(filename, format="png", cleanup=True)  # Save as PNG
    print(f"Tree visualization saved as {filename}.png")

# This will create an image of the binary tree structure for easy reference.
visualize_tree(tree)