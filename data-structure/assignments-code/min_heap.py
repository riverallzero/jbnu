from typing import Union
import math


class Node:
    def __init__(self, data: Union[int, 'TreeNode']):
        self.data: Union[int, 'TreeNode'] = data
        self.next: Union['Node', None] = None
        self.prev: Union['Node', None] = None


class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Union['TreeNode', None] = None
        self.right: Union['TreeNode', None] = None
        self.parent: Union['TreeNode', None] = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None

    def append(self, data: Union[int, TreeNode]) -> None:
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self) -> None:
        if self.head is None:
            print('List is empty')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def insert(self, data: Union[int, TreeNode], index: int) -> None:
        new_node = Node(data)
        p = self.head

        for _ in range(index - 1):
            p = p.next

        new_node.next = p.next
        new_node.prev = p
        p.next.prev = new_node
        p.next = new_node

    def delete(self, index: int) -> None:
        p = self.head

        for _ in range(index):
            p = p.next

        p.prev.next = p.next
        p.next.prev = p.prev

    def contains(self, data: Union[int, TreeNode]) -> bool:
        p = self.head

        while p is not None:
            if p.data == data:
                return True
            p = p.next

        return False

    def search(self, data: Union[int, TreeNode]) -> list:
        find_element_index_list = []
        p = self.head
        index = 0

        while p is not None:
            if p.data == data:
                find_element_index_list.append(index)
            index += 1
            p = p.next

        return find_element_index_list

    def __getitem__(self, item: int) -> Union[int, TreeNode]:
        p = self.head
        for _ in range(item):
            p = p.next

        return p.data

    def size(self) -> int:
        size_count = 0
        p = self.head
        while p is not None:
            size_count += 1
            p = p.next

        return size_count

    def print_elements(self) -> str:
        elements_list = []
        p = self.head
        while p is not None:
            elements_list.append(p.data)
            p = p.next

        return ' '.join([str(val) for val in elements_list])


class MinHeap:
    def __init__(self):
        self.root: Union[TreeNode, None] = None
        self.node_list = DoubleLinkedList()
        self.node_count = 0

    def size(self) -> int:
        return self.node_count

    def get_height(self, node: Union[TreeNode, None]) -> int:
        if node is None:
            return 0
        l_height = self.get_height(node.left)
        r_height = self.get_height(node.right)
        return max(l_height, r_height) + 1

    def height(self) -> int:
        return self.get_height(self.root)

    def get_parent(self) -> Union[TreeNode, None]:
        if self.node_count == 0:
            return None
        parent_index = (self.node_count - 1) // 2
        current = self.node_list.head
        for _ in range(parent_index):
            current = current.next
        return current.data

    def heapify_upstream(self, node: TreeNode) -> None:
        while node.left:
            smallest_child = node.left
            if node.right and node.right.data < node.left.data:
                smallest_child = node.right
            if node.data <= smallest_child.data:
                break
            node.data, smallest_child.data = smallest_child.data, node.data
            node = smallest_child

    def heapify(self) -> None:
        self.heapify_upstream(self.root)

    def insert(self, value: Union[int, float, str]) -> None:
        new_node = TreeNode(value)
        self.node_list.append(new_node)
        if self.node_count == 0:
            self.root = new_node
        else:
            parent = self.get_parent()
            new_node.parent = parent
            if parent.left is None:
                parent.left = new_node
            elif parent.right is None:
                parent.right = new_node
            else:
                raise IndexError("Parent node is full")
        self.node_count += 1
        self.heapify()

    def get(self) -> Union[int, float, str]:
        if self.node_count == 0:
            raise IndexError("Heap is empty")
        root_value = self.root.data
        if self.node_count == 1:
            self.root = None
            self.node_list.remove()
        else:
            last_node = self.node_list.tail.data
            self.root.data = last_node.data
            if last_node.parent.left == last_node:
                last_node.parent.left = None
            else:
                last_node.parent.right = None
            self.node_list.remove()
        self.node_count -= 1
        self.heapify()
        print(f"[get] Root Value: {root_value}")
        return root_value

    def in_order(self, node: Union[TreeNode, None], elements: list) -> None:
        if node:
            self.in_order(node.left, elements)
            elements.append(node.data)
            self.in_order(node.right, elements)

    def pre_order(self, node: Union[TreeNode, None], elements: list) -> None:
        if node:
            elements.append(node.data)
            self.pre_order(node.left, elements)
            self.pre_order(node.right, elements)

    def post_order(self, node: Union[TreeNode, None], elements: list) -> None:
        if node:
            self.post_order(node.left, elements)
            self.post_order(node.right, elements)
            elements.append(node.data)

    def printElement(self, order: str) -> None:
        elements = []

        if order == "inorder":
            self.in_order(self.root, elements)
        elif order == "preorder":
            self.pre_order(self.root, elements)
        elif order == "postorder":
            self.post_order(self.root, elements)
        else:
            raise ValueError("Only accept inorder, preorder, postorder!")

        results = f"[{order}] "
        for i in range(len(elements)):
            results += str(elements[i])
            if i != len(elements) - 1:
                results += " => "

        print(results)

    def print_tree(self) -> None:
        array_size = int(math.pow(2, self.height()))
        elements = [None] * array_size
        is_fill = [0] * array_size

        def print_heap(node: Union[TreeNode, None], level: int) -> None:
            if not node:
                return
            elements[level] = node.data
            is_fill[level] = 1
            print_heap(node.left, 2 * level)
            print_heap(node.right, 2 * level + 1)

        print_heap(self.root, 1)

        print("----tree----")
        for i in range(1, array_size):
            print(elements[i] if is_fill[i] else "X", end=" ")
            if math.log2(i + 1).is_integer():
                print()
        print("------------")


if __name__ == "__main__":
    minheap = MinHeap()

    minheap.insert(3)
    minheap.insert(4)
    minheap.insert(1)
    minheap.insert(5)
    minheap.insert(6)
    print("Size:", minheap.size())
    print("Height:", minheap.height())
    minheap.print_tree()
    minheap.printElement("inorder")

    minheap.get()
    minheap.print_tree()

    minheap.insert(7)
    minheap.print_tree()
    minheap.printElement("postorder")
