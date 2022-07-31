"""
Simple Queue implementation using Python's list
"""


class Deque:
    def __init__(self) -> None:
        self.deque = list()

    def insert_rear(self, item):
        # Time Complexity: O(n)
        self.deque.insert(0, item)

    def insert_front(self, item):
        # Time Complexity: O(1)
        self.deque.append(item)

    def remove_rear(self):
        # Time Complexity: O(n)
        return self.deque.pop(0)

    def remove_front(self):
        # Time Complexity: O(1)
        return self.deque.pop()

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return self.deque == []

    def display(self):
        return [item for item in self.deque]


if __name__ == "__main__":
    object = Deque()
    object.insert_front("Data")
    object.insert_rear("Cat")
    object.insert_rear("Robot")
    object.insert_front("Data Dance")
    print(object.display())
    print(object.remove_front())
    print(object.display())
    print(object.remove_rear())
    print(object.display())
