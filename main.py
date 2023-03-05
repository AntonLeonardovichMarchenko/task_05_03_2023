"""
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
Вывести цифры числа на каждой строчке.

Найти сумму цифр числа.
Найти произведение цифр числа.
Дать ответ на вопрос: есть ли среди цифр числа 5?
Найти максимальную цифру в числе
Найти количество цифр 5 в числе

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

def script_2():

    class Summator:
        def __init__(self, n = 100):
            self.N = n

        def goSumm(self):
            self.result = 0
            for i in range(0, self.N):
                self.result += i

        def TypeTheResult(self):
            print(f'\nThe result of the summ in range(0, {self.N}) is {self.result}')

    summ = Summator()
    summ.goSumm()
    summ.TypeTheResult()

def script_3():

    class Productor:

        nn = None
        res = None
        digitsArray = []

        def __init__(self, n = 10):
            self.N = n + 1
            Productor.nn = n

        def goProduction(self):
            self.result = 1
            for i in range(1, self.N):
                self.result *= i

        def TypeTheResult(self):
            print(f'\nThe result of the product in range(1, {self.N}) is {self.result}')
            return self.result

    prod = Productor()
    prod.goProduction()
    Productor.res = prod.TypeTheResult()

    while Productor.res > 0:
        res = Productor.res % 10
        #print(res)
        Productor.res //= 10
        Productor.digitsArray.append(res)

    for i in range(len(Productor.digitsArray) - 1, -1, -1):
        print(Productor.digitsArray[i])

def script_00():

    class DigitsGenerator:
        res = None
        digitsArray = []

        def __init__(self, n=10):
            order = 1
            self.digit = 0
            for i in range(1, n+1):
                r = random.randint(0, 10)
                if order > 1:
                    self.digit += r*order
                else:
                    self.digit += r
                order *= 10
                print(self.digit)

        def DigitParser(self):
            while DigitsGenerator.res > 0:
                res = DigitsGenerator.res % 10
                # print(res)
                DigitsGenerator.res //= 10
                DigitsGenerator.digitsArray.append(res)

        def SummFinder(self):
            self.DigitParser()
            summ = 0
            print(f'=========================')
            for i in range(0, len(DigitsGenerator.digitsArray)):
                summ += DigitsGenerator.digitsArray[i]
                print(f'{DigitsGenerator.digitsArray[i]} +> {summ}')
            self.digit = summ

        def ProdFinder(self):
            self.DigitParser()
            prod = 1
            print(f'=========================')
            for i in range(0, len(DigitsGenerator.digitsArray)):
                if DigitsGenerator.digitsArray[i] > 0:
                    prod *= DigitsGenerator.digitsArray[i]
                print(f'{DigitsGenerator.digitsArray[i]} *> {prod}')
            self.digit = prod

        def FiveFinder(self):
            self.DigitParser()
            nFives = 0
            print(f'=========================')
            for i in range(0, len(DigitsGenerator.digitsArray)):
                print(f'{DigitsGenerator.digitsArray[i]}')
                if DigitsGenerator.digitsArray[i] == 5:
                    nFives += 1
                    print(f'{DigitsGenerator.digitsArray[i]} *> {nFives}')

            self.digit = nFives
            print('')

        def MaxFinder(self):
            self.DigitParser()
            maxValue = 0
            print(f'=========================')
            for i in range(0, len(DigitsGenerator.digitsArray)):

                if DigitsGenerator.digitsArray[i] > maxValue:
                    maxValue = DigitsGenerator.digitsArray[i]
                    print(f'{DigitsGenerator.digitsArray[i]} >> {maxValue}')
                else:
                    print(f'{DigitsGenerator.digitsArray[i]}')


            self.digit = maxValue
            print('')

        def TypeTheResult(self):
            print(self.digit)
            return self.digit

    dg = DigitsGenerator()
    DigitsGenerator.res = dg.TypeTheResult()
    dg.SummFinder()
    dg.TypeTheResult()
    dg.ProdFinder()
    dg.TypeTheResult()
    dg.FiveFinder()
    dg.TypeTheResult()
    dg.MaxFinder()
    dg.TypeTheResult()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    script_0()
    script_1()
    script_2()
    script_3()
    script_00()

