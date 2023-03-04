"""
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
Вывести цифры числа на каждой строчке.
"""
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zs_maker = ZerosMaker(5, 9)
    zs_maker.print_hi('PyCharm')
    zs_maker.zeros()
