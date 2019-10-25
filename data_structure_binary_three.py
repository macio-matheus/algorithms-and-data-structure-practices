class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Three:
    def __init__(self):
        self.top = None
        self._size = 0

    def __len__(self):
        return self._size
