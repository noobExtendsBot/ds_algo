"""
1. Base Case
2. Change state using data that is being worked upon
3. Recursive call
"""

class ListSum:
    # [1,2,3,4,5]
    def solve(self, nList):
        if len(nList) == 1:
            return nList[0]
        else:
            return nList[0] + self.solve(nList[1:])

if __name__ == "__main__":
    sum = ListSum()
    print(sum.solve([2,3,4,5]))