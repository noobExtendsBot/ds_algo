"""
Problem Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


class Solution:
    def calculate(self, operand_1, operand_2, operator):
        if operator == '+':
            return operand_1 + operand_2
        elif operator == '-':
            return operand_1 - operand_2
        elif operator == '*':
            return operand_1 * operand_2
        else:
            return int(operand_1 / operand_2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            if i in "+-*/":
                num_2, num_1 = stack.pop(), stack.pop()
                res = self.calculate(num_1, num_2, i)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
