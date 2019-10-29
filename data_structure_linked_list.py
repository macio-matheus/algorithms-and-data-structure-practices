class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elemen):

        if self.head:
            pointer = self.head

            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elemen)
        else:
            self.head = Node(elemen)

        self._size = self._size + 1

    def get(self, index: int):
        if index > (self._size - 1):
            return ValueError("Index error")

        if self.head:
            pointer, i = self.head, 0
            last_node = pointer
            while pointer.next:
                if index == i:
                    return last_node
                last_node = pointer.next
                i = i + 1

    def __len__(self):
        return self._size

    # TODO: Imlement methos to get values by index


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(7)

    print(my_list.get(2))
