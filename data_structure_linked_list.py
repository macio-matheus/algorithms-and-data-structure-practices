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

    def append(self, el):
        if self.head:
            pointer = self.head
            j = 0
            while pointer.next:
                pointer = pointer.next
                print("j: ", j)
            print("Pointer last: ", pointer, "EL: ", el)
            pointer.next = Node(el)
            print("Pointer last: ", pointer.next, "EL: ", el)
        else:
            self.head = Node(el)

        self._size = self._size + 1

    def get(self, index: int):
        if index > (self._size - 1):
            return ValueError("Index error")

        pointer = self.head
        for _ in range(index):
            if pointer:
                pointer = pointer.next

        return pointer

    def __len__(self):
        return self._size


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(7)
    my_list.append(10)

    print("Len: ", len(my_list))
    for i in range(len(my_list)):
        print(f"Element in {i} position: ", my_list.get(i))

    print(my_list.get(0), my_list.get(1), my_list.get(2))
