class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)


if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.root.left = Node(15)
    tree.root.right = Node(20)

    print(tree.root, tree.root.left, tree.root.right)
