class BinaryTreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def depth_first_value(root: BinaryTreeNode) -> list:
    stack = []
    stack.append(root)
    results = []
    while len(stack):
        node: BinaryTreeNode = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        results.append(node.value)
    return results

def breadth_first_value(root: BinaryTreeNode) -> list:
    queue = []
    queue.append(root)
    results = []
    while len(queue):
        node: BinaryTreeNode = queue.pop(0)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        results.append(node.value)
    return results

def get_inorder(root: BinaryTreeNode, result: list) -> list:
    if root is None:
        return result
    result = get_inorder(root.left, result)
    result.append(str(root.value))
    result = get_inorder(root.right, result)
    return result

def inorder_iterative(root: BinaryTreeNode) -> str:
    result = []
    result = get_inorder(root, result)
    return " ".join(result)

def inorder_successor_bst(root: BinaryTreeNode, d):
    result = []
    result = get_inorder(root, result)
    try:
        index = result.index(d)
    except ValueError:
        return None
    else:
        return result[index + 1] if index < (len(result) - 1) else None
