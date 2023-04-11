# Написать программу, которая определяет, можно ли от шоколадки n * m долек
# отломить k долек. Можно сделать только один разлом.

print("Введите размеры шоколадки: ")
n = input()
m = input()
k = int(input())
counter = 0
counter_2 = 0
array = []
for i in range(int(n) - 1):
    for j in range(int(m)):
        counter += 1
    array.append(counter)
for i in range(int(m) - 1):
    for j in range(int(n)):
        counter_2 += 1
    if counter_2 in array:
        continue
    array.append(counter_2)
print(f"Возможные вариации разлома --> {array}")
if k in array:
    print(f"Можно получить {k} долек")
else:
    print(f"Невозможно получить {k} долек с помощью одного разлома")
