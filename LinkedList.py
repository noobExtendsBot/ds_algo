"""
A simple implementation of Linked List
"""


class Node:
    """
    A Node class for data and next
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Order is important, either increasing or decreasing
    Assumption: Sorted in increasing order
    """

    def __init__(self):
        self.head = None

    def add(self, data):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.data > data:
                found = True
            else:
                previous = current
                current = current.next

        new_node = Node(data)
        if previous is not None:
            previous.next = new_node
            new_node.next = current
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True  # item found
            elif current.data > data:
                return False  # item not in the list
            current = current.next

    def display(self):
        # display all elements of the LinkedList O(n)
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("\n")
        return


if __name__ == "__main__":
    llist = LinkedList()
    llist.add(2)
    llist.add(10)
    llist.add(1)
    llist.display()
    if llist.search(1):
        print("element found")
    if llist.search(10):
        print("element found")
    if llist.search(0):
        print("element found")
    else:
        print("element not found")
    llist.display()
