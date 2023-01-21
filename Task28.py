# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    if b == 0:
        return a
    else:
        return a + sum(1, b - 1)


def numberA():
    a = int(input('Введите число A: '))
    if a < 0:
        print('Неверно! Введите целое неотрицательное число: ')
        return numberA()
    else:
        return a


def numberB():
    b = int(input('Введите число B: '))
    if b < 0:
        print('Неверно! Введите целое неотрицательное число: ')
        return numberB()
    else:
        return b


A = numberA()
B = numberB()
result = sum(A, B)
print(f'{A} + {B} = {result}')