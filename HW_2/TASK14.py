# Вывести все целые степени цифры 2, не првевосходящие числа N

N = int(input("Введите число N: "))
degree = 0
res = 0
while res < N:
    res = pow(2, degree)
    if res >= N:
        break
    print(res)
    degree += 1
