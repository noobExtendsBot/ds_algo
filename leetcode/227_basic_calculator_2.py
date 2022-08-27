"""
Problem Link: https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:
    precedence_mapper = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def calc(self, operand_1, operand_2, operator):
        if operator == "+":
            return operand_1 + operand_2
        elif operator == "-":
            return operand_1 - operand_2
        elif operator == "*":
            return operand_1 * operand_2
        else:
            return int(operand_1 / operand_2)

    def eval_postfix(self, s: str) -> int:
        stack = list()
        for i in s.split(" "):
            if i in "*/+-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = self.calc(int(operand1), int(operand2), i)
                stack.append(res)
            elif i != " ":
                stack.append(i)
        return stack[0]

    def check_precedence(self, op1, op2) -> bool:
        if self.precedence_mapper[op1] >= self.precedence_mapper[op2]:
            return True
        return False

    def infix_to_postfix(self, s: str) -> int:
        sList = [i for i in s.replace(" ", "")]
        output_stack = list()
        operator_stack = list()

        for i in sList:
            if i in "+-/*":
                # add a space to mark end of item
                output_stack.append(" ")
                try:
                    while len(operator_stack) > 0 and self.check_precedence(
                            operator_stack[-1], i):
                        output_stack.append(operator_stack.pop())
                        output_stack.append(" ")
                    operator_stack.append(i)

                except IndexError:
                    operator_stack.append(i)

            else:
                output_stack.append(i)

        while len(operator_stack) > 0:
            # add space to mark the end of previous items
            output_stack.append(" ")
            output_stack.append(operator_stack.pop())

        res = self.eval_postfix("".join(output_stack))
        return res

    def calculate(self, s: str) -> int:
        return self.infix_to_postfix(s)
