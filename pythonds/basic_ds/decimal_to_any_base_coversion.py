"""
Convert decimal to base 2 to 16
"""

class DecimalToBinary():
    def convert(self, decimal:int, base:int) -> str:
        slist = list()
        digits = "0123456789ABCDE"
        while decimal > 0:
            rem = decimal%base
            slist.append(rem)
            decimal = decimal//base
        res = ''.join([digits[i] for i in slist])
        return res[::-1]

if __name__ == "__main__":
    object = DecimalToBinary()
    print(object.convert(233, 2))
    print(object.convert(233, 16))
    print(object.convert(25, 8))
    print(object.convert(256, 16))


