"""
Simple Queue implementation using Python's list
Enqueue Time Complexity: O(n) at start of the list
Dequeue Time Complexity: O(1) at end of the list
"""


class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        # time complexity O(n)
        self.queue.insert(0, item)

    def dequeue(self):
        self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return [item for item in self.queue][::-1]


if __name__ == "__main__":
    object = Queue()
    object.enqueue(20)
    object.enqueue(10)
    object.enqueue(1)
    object.dequeue()
    print(object.display())
    object.enqueue(2)
    object.enqueue(3)
    print(object.display())
