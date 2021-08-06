class Tree:
    def __init__(self, node, left = None, right = None):
        self.val = node
        self.left = left
        self.right = right


def inorder(root):
    """
    root: Tree node
    """
    current = root
    my_stack = []

    while True:
        if current is not None:
            my_stack.append(current)
            current = current.left

        elif len(my_stack) > 0:
            current = my_stack.pop()
            print(current.val)
            current = current.right

        else:
            break

def preorder(root):
    if root is None:
        return

    node_stack = []
    node_stack.append(root)

    while len(node_stack) > 0:
        current_node = node_stack.pop()
        print(current_node.data, end = ' ')

        if current_node.right is not None:
            node_stack.append(current_node)
        if current_node.left is not None:
            node_stack.append(current_node)
