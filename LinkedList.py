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


class UnorderedList:
    """
    An unordered list, most easy operation append at head
    """

    def __init__(self):
        # a pointer to first Node
        self.head = None

    def add(self, data):
        # Add new item to head time complexity O(1)
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            # next node saves the previous node
            # that will be next_node for new node
            next_node = self.head
            self.head = new_node
            new_node.next = next_node
        return True

    def display(self):
        # display all elements of the LinkedList O(n)
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("\n")
        return

    def remove(self, data):
        # Assumption element exists in the LinkedList
        # remove a particular element from the LinkedList O(n)
        current = self.head
        previous = None
        found = False
        while current is not None and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            # first element
            self.head = current.next
        else:
            previous.next = current.next
        del current
        return True


if __name__ == "__main__":
    llist = UnorderedList()
    llist.add(5)
    llist.display()
    llist.add(25)
    llist.add(15)
    llist.add(50)
    llist.add(11)
    llist.add(55)
    llist.display()
    llist.remove(55)
    llist.display()
    llist.remove(5)
    llist.display()
    llist.remove(15)
    llist.display()
