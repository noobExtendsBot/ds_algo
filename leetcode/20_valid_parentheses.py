"""
Problem link: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        slist = list()
        balanced = True
        closer_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        # closers = ')]}'
        try:
            for index, value in enumerate(s):
                if value in "{[(":
                    slist.append(value)
                else:
                    pop_val = slist.pop()
                    if value != closer_dict[pop_val]:
                        balanced = False
                        break
        except IndexError:
            balanced = False

        if len(slist) != 0:
            balanced = False

        return balanced


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("{({([][])}())}"))
    print(sol.isValid("[{()]"))
    print(sol.isValid("[{("))
    print(sol.isValid("}]"))
