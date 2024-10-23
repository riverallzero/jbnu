from typing import Union


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Union[Node, None] = None
        self.prev: Union[Node, None] = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None

    def append(self, data: int) -> None:
        newNode = Node(data)

        newNode.next = None

        if self.head is None:
            self.head = newNode
            self.tail = newNode

            newNode.prev = None
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def remove(self) -> None:
        if self.head == None:
            print('List is empty')

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert(self, data: int, index: int) -> None:
        newNode = Node(data)
        p = self.head

        for i in range(index - 1):
            p = p.next

        newNode.next = p.next
        newNode.prev = p

        p.next.prev = newNode
        p.next = newNode

    def delete(self, index: int) -> None:
        p = self.head

        for i in range(index):
            p = p.next

        p.prev.next = p.next
        p.next.prev = p.prev

    def contains(self, data: int) -> bool:
        p = self.head

        while p is not None:
            if p.data == data:
                return True
            p = p.next

            if p is None:
                return False

    def search(self, data: int) -> list:
        find_element_index_list = []
        p = self.head
        index = 0

        while p is not None:
            if p.data == data:
                find_element_index_list.append(index)
            index += 1
            p = p.next

        return find_element_index_list

    def __getitem__(self, item: int) -> int:
        p = self.head
        for i in range(item):
            p = p.next

        return p.data

    def size(self):
        size_count = 0
        p = self.head
        while p != None:
            size_count += 1
            p = p.next

        return size_count

    def printElements(self) -> None:
        elements_list = []
        p = self.head
        while p != None:
            elements_list.append(p.data)
            p = p.next

        print(' '.join([str(val) for val in elements_list]))


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.printElements()  # 1 2 3 4 5 1 2 3 4 5
    dll.remove()
    dll.printElements()  # 1 2 3 4 5 1 2 3 4
    dll.insert(3, 2)
    dll.printElements()  # 1 2 3 3 4 5 1 2 3 4
    dll.delete(2)
    dll.printElements()  # 1 2 3 4 5 1 2 3 4
    print(dll.contains(3))  # True
    print(dll.contains(6))  # False
    print(dll.search(3))  # [2, 7]
    print(dll.search(4))  # [3, 8]
    print(dll.search(6))  # []
    print(dll.search(1))  # [0, 5]
    print(dll.search(5))  # [4, 9]
    print(dll.search(2))  # [1, 6]
    print(dll.search(7))  # []
    print(dll.search(8))  # []

    print(dll[0])  # 1
    print(dll[1])  # 2
    print(dll[2])  # 3
    print(dll[3])  # 4
