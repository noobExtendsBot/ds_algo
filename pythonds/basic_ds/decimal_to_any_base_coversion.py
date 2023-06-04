"""
Convert decimal to base 2 to 16
"""


class DecimalToBinary:
    res = list()

    def convert(self, decimal: int, base: int) -> str:
        slist = list()
        digits = "0123456789ABCDE"
        while decimal > 0:
            rem = decimal % base
            slist.append(rem)
            decimal = decimal // base
        res = "".join([digits[i] for i in slist])
        return res[::-1]

    def convert_recursion(self, n, base):
        arr_string = "0123456789ABCDE"
        if n // base == 0:
            self.res.append(arr_string[n])
            return

        pos = self.convert_recursion(n // base, base)
        self.res.append(arr_string[n % base])
        return


if __name__ == "__main__":
    object = DecimalToBinary()
    print(object.convert(233, 2))
    print(object.convert(233, 16))
    print(object.convert(25, 8))
    print(object.convert(256, 16))

    # object.convert_recursion(233, 2)
    object.convert_recursion(233, 16)
    print(object.res)
    # print(object.convert_recursion(233, 16))
    # print(object.convert_recursion(25, 8))
    # print(object.convert_recursion(256, 16))
