def binar_tree(r):
    return [r, [], []]


def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


if __name__ == "__main__":
    r = binary_tree(5)
    insert_left(r, 3)
    insert_left(r, 4)
    insert_right(r, 7)
    insert_right(r, 8)
    print(get_left_child(r))
