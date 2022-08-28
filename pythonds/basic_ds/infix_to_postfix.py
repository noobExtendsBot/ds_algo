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

    def has_greater_precedence(self, op1, op2):
        if self.precedence_mapper[op1] >= self.precedence_mapper[op2]:
            return True
        return False

    def infix_to_postfix(self, s: str) -> str:
        sList = [i for i in s.replace(" ", "")]
        output = []
        operator_stack = []
        # print(sList)
        for i in sList:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                output.append(i)
            else:
                while len(operator_stack) > 0 and self.has_greater_precedence(
                        operator_stack[-1], i):
                    output.append(operator_stack.pop())
                operator_stack.append(i)

        while len(operator_stack) > 0:
            output.append(operator_stack.pop())

        return ''.join(output)
        # print(''.join(output))
        # print(operator_stack)


if __name__ == "__main__":
    sol = MySolution()
    print(sol.infix_to_postfix("A * B + C * D"))
    print(sol.infix_to_postfix("A + B * C"))
