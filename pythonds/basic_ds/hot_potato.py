from Queue import Queue


def solve_hot_potato(name_list: list, n: int) -> str:
    queue_obj = Queue()

    for i in name_list:
        queue_obj.enqueue(i)

    while queue_obj.size() > 1:
        for _ in range(n):
            queue_obj.enqueue(queue_obj.dequeue())
        queue_obj.dequeue()
    return queue_obj.dequeue()


if __name__ == "__main__":
    print(solve_hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
