from BinaryTree import *
import pytest

@pytest.fixture
def root() -> BinaryTreeNode:
    node_root = BinaryTreeNode("A")
    node_b = BinaryTreeNode("B")
    node_c = BinaryTreeNode("C")
    node_d = BinaryTreeNode("D")
    node_e = BinaryTreeNode("E")
    node_f = BinaryTreeNode("F")
    node_root.right = node_c
    node_root.left = node_b
    node_b.right = node_d
    node_b.left = node_e
    node_c.right = node_f
    return node_root

def test_depth_first_value(root: BinaryTreeNode):
    """
        Test Algorithm Depth First Value
        source: FreeCodeCamp BinaryTree
    """
    results = depth_first_value(root)
    assert results == ["A", "B", "E", "D", "C", "F"]

def test_breadth_first_value(root: BinaryTreeNode):
    results = breadth_first_value(root)
    assert results == ['A', 'C', 'B', 'F', 'D', 'E']

def test_compare_two_nodes(root: BinaryTreeNode):
    root2 = BinaryTreeNode("A")
    result1 = depth_first_value(root)
    result2 = depth_first_value(root2)
    assert result1 != result2

def test_inorder_iterative(root: BinaryTreeNode):
    results = inorder_iterative(root)
    assert results == "E B D A C F"

def test_inorder_search_bst(root: BinaryTreeNode):
    value = inorder_successor_bst(root, "D")
    assert value == "A"