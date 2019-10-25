class Node:
    def __init__(self, data: str):
        self.val = data
        self.next = None


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

    def __len__(self):
        return self._size

    # TODO: Imlement methos to get values by index


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(7)

    print(len(my_list))
