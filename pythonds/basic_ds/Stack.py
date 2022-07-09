"""
Stack implementation using Python
"""


class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return [item for item in self.items]


if __name__ == "__main__":
    my_list = Stack()
    my_list.push(4)
    my_list.push(5)
    my_list.push(3)
    my_list.push(2)
    print(my_list.pop())
    print(my_list.display())
