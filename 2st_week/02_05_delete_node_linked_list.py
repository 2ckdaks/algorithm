class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        if index == 0:
            next_node = self.head
            self.head = Node(value)
            self.head.next = next_node

        else:
            new_node = Node(value)
            index_minus_1_node = self.get_node(index - 1)

            next_node = index_minus_1_node.next

            index_minus_1_node.next = new_node
            new_node.next = next_node
            print("index 위치에 value를 가진 node를 추가")

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            index_node = self.get_node(index)
            next_node = index_node.next

            prev_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()

# linked_list.add_node(0, 6)
# linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()