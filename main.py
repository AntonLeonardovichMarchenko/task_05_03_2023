"""
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
Вывести цифры числа на каждой строчке.
"""
import random

def script_0():
    class ZerosMaker:

        def __init__(self, m, n):
            self.m = m
            self.n = n

        def print_hi(self, name):
            print(f'Hi, {name}')

        def zeros(self):
            print(f'm == {self.m}, n == {self.n} \n')
            strz = str(0)*self.m
            for i in range(0, self.n):
                print(f'{i}   {strz}')

    zs_maker = ZerosMaker(5, 9)
    zs_maker.print_hi('PyCharm')
    zs_maker.zeros()

def script_1():
    class fiveTester:

        def __init__(self):
            self.nDigits = 100
            self.digits = []
            self.n_5 = 0
            for i in range(0, self.nDigits):
                self.digits.append(random.randint(0, 10))

        def doIt(self,nDigits):
            n_5 = 0
            for i in range(0, nDigits):
                if self.digits[i] == 5:
                    self.n_5 += 1

        def typeTheResult(self):
            print(f'\nquantity of 5 is {self.n_5}')

    fvTester = fiveTester()
    fvTester.doIt(fvTester.nDigits)
    fvTester.typeTheResult()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    script_0()
    script_1()


