# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


N = int(input("Введите количество элементов первого множества "))
M = int(input("Введите количество элементов второго множества "))

list_a = []
list_b = []

for i in range(N):
    a = int(input("Введите число первого списка: "))
    list_a.append(a)
print(list_a)
for i in range(M):
    b = int(input("Введите число второго списка: "))
    list_b.append(b)
print(list_b)

set_a = set(list_a)
set_b = set(list_b)

print(set_a)
print(set_b)

new_set = set_a.union(set_b)
new_list = list(new_set)
new_list.sort()

print(new_list)


