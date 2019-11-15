class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, data=None):
        self.root = Node(data)


if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.root.left = Node(15)
    tree.root.right = Node(20)

    print(tree.root, tree.root.left, tree.root.right)
    # (a + (b * ((c /d ) - e)))
    tree = BinaryTree()
    node_one = Node('a')
    node_two = Node('+')
    node_three = Node('*')
    node_four = Node('b')
    node_five = Node('-')
    node_six = Node('/')
    node_seven = Node('c')
    node_eigth = Node('d')
    node_nine = Node('e')

    tree.root = node_two
    node_two.left = node_one
    node_two.right = node_three
    node_three.left = node_four
    node_three.right = node_six
    node_six.left = node_seven
    node_six.right = node_eigth


