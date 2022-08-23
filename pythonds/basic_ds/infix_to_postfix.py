"""
Infix to Postfix conversion
"""


class MySolution:
    precedence_mapper = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def infix_to_postfix(self, s: str) -> str:
        sList = [i for i in s.replace(" ", "")]
        output = []
        operator_stack = []
        # print(sList)
        for i in sList:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                output.append(i)
            else:
                try:
                    last_operator = operator_stack.pop()
                    # if precedence of operator in stack is equal to or greater than current
                    # then push it to output stack
                    if self.precedence_mapper[i] > self.precedence_mapper[last_operator]:
                        operator_stack.append(last_operator)
                        operator_stack.append(i)
                    else:
                        output.append(last_operator)
                        operator_stack.append(i)
                except IndexError:
                    operator_stack.append(i)

        if len(operator_stack) != 0:
            while len(operator_stack) > 0:
                output.append(operator_stack.pop())

        return ''.join(output)
        # print(''.join(output))
        # print(operator_stack)


if __name__ == "__main__":
    sol = MySolution()
    print(sol.infix_to_postfix("A * B + C * D"))
    print(sol.infix_to_postfix("A + B * C"))
