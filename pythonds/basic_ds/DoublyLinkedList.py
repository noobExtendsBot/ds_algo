"""
A simple implementation of Doubly LinkedList
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node

    def insert_at_tail(self, data):
        current = self.head
        while current.next is not None:
            current = current.next

        new_node = Node(data)
        current.next = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print("\n")

    def print_reverse(self, current=None):
        # using recursion
        # if current == None:
        #     return
        # self.print_reverse(current=current.next)
        # print(current.data, end=" ")

        # using prev pointer
        # Traverse to last Node
        prev = None
        while current is not None:
            prev = current
            current = current.next

        # Traverse back to first Node using prev pointer
        while prev is not None:
            print(prev.data, end=" ")
            prev = prev.prev
        print("\n")


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_head(10)
    llist.insert_at_head(5)
    llist.insert_at_head(1)
    llist.print()
    llist.print_reverse(llist.head)
    llist.insert_at_tail(25)
    llist.print()
