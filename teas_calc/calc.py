from arith import *


class Calc():

    @staticmethod
    def calc(arg1, arg2, operator):

        if operator == "1":
            return Add.add(arg1, arg2)
        elif operator == "2":
            return Sub.sub(arg1, arg2)
        elif operator == "3":
            return Mul.mul(arg1, arg2)
        elif operator == "4":
            return Div.div(arg1, arg2)
        else:
            raise ValueError("Illegal Argment!")
