
"""
Poblem Link: https://leetcode.com/problems/implement-stack-using-queues/
"""


class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, x):
        self.queue.insert(0, x)

    def dequeue(self):
        return self.queue.pop()

    def top(self):
        return self.queue[-1]


class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        while len(self.queue1.queue) > 0:
            self.queue2.enqueue(self.queue1.dequeue())

        self.queue1.enqueue(x)

        while len(self.queue2.queue) > 0:
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self) -> int:
        return self.queue1.dequeue()

    def top(self) -> int:
        return self.queue1.top()

    def empty(self) -> bool:
        return len(self.queue1.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
