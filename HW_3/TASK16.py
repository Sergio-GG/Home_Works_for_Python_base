 # Сколько раз встречается число X в массиве A[1, N].
 # Ввести количество элементов в массиве - N.
import random
array = []
counter = 0
N = int(input("Введите количество элементов: "))
X = int(input("Введите искомое число: "))
for i in range(N):
    a = random.randint(-3,3)
    if X == a:
        counter += 1
    array.append(a)
print(f"Количество чисел в массиве {N}")
print(array)
print(f"Искомое число: {X}")
print(f"Встречается раз --> {counter}")

