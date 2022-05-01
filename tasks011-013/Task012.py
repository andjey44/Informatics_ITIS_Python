from functools import partial


class Homework:
    def calculator(self,
             change_1: int = 0, oper1: str = '+',
             change_2: int = 0, oper2: str = '+',
             change_3: int = 0, oper3: str = '+',
             change_4: int = 0, oper4: str = '+',
             change_5: int = 0) -> int:
        logic = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '*': lambda a, b: a * b,
                 '/': lambda a, b: a / b}
        return logic[oper4](logic[oper3](logic[oper2](logic[oper1](change_1, change_2), change_3), change_4), change_5)

    def special_calculator(self, change_1: int):
        def oper_1(oper1: str):
            def change_2(change_2: int):
                def oper_2(oper2: str):
                    def change_3(change_3: int):
                        def oper_3(oper3: str):
                            def change_4(change_4: int):
                                def oper_4(oper4: str):
                                    def change_5(change_5: int) -> int:
                                        logic = {'+': lambda a, b: a + b,
                                                 '-': lambda a, b: a - b,
                                                 '*': lambda a, b: a * b,
                                                 '/': lambda a, b: a / b}
                                        return logic[oper4](logic[oper3](logic[oper2](logic[oper1](change_1, change_2),
                                                                                   change_3), change_4), change_5)
                                    return change_5
                                return oper_4
                            return change_4
                        return oper_3
                    return change_3
                return oper_2
            return change_2
        return oper_1


sc = Homework()
print(sc.calculator(1, '+', 2, '-', 3, '+', 4, '*', 5))
print(sc.special_calculator(1)('*')(2)('+')(3)('-')(4)('+')(5))

calculator_par = partial(sc.calculator, change_1=1, change_2=2, change_3=3, change_4=4, change_5=5)
print('(((1+2)+3)*4)+5 =', calculator_par(oper1='+', oper2='+', oper3='*', oper4='+'))
print('(((1*2)+3)-4)/5 =', calculator_par(oper1='*', oper2='+', oper3='-', oper4='/'))
print('(((1-2)-3)*4)*5 =', calculator_par(oper1='-', oper2='-', oper3='*', oper4='*'))