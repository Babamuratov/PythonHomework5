# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(A, B):
    if B == 0:
        return 1
    elif B > 0:
        return A * degree(A, B - 1)
    else:
        return 1 / A * degree(1 / A, abs(B) - 1)

A = int(input('Введите число: '))
B = int(input('Введите степень числа: '))
print(f'{A} в степени {B} = {degree(A, B)}')