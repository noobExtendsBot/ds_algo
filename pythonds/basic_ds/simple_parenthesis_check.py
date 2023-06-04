from Stack import Stack


def check_parenthesis(symbols):
    my_list = Stack()
    balanced = True
    try:
        for item in symbols:
            if item == "(":
                my_list.push(item)
            else:
                my_list.pop()
    except IndexError:
        balanced = False

    if my_list.is_empty() and balanced:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_parenthesis("((()))"))
    print(check_parenthesis("(()"))
    print(check_parenthesis("))"))
    print(check_parenthesis("(("))
