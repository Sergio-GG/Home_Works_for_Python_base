# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))


def degree(a, b):
    if b == 1:
        return a
    return a * (degree(a, b - 1))


res = degree(num_1, num_2)

print(f"Результат равен {res}")
