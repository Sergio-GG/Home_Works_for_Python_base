# Найти самое близкое число из массива к заданному числу


import random
array = []
new_array = []
index = 0
N = int(input("Введите количество элементов: "))
X = int(input("Введите искомое число: "))
max_num = 0
min_num = 0
for i in range(N):                                                  # Заполняем список
    a = random.randint(-40, 40)
    array.append(a)


new_array.extend(array)                                             # Создаем копию списка
new_array.append(X)                                                 # и добавляем наше число в список
new_array.sort()                                                    # Сортируем список

print(f"Количество чисел в списке --> {N}")
array.sort()                                                        # Сортируем первый список для удобства чтения
print(array)
print(f"Искомое число --> {X}")

for j in range(len(new_array)):
    if new_array[index] == X:
        if 0 < index < len(new_array) - 1:                          # Находим числа справа и слева от числа
            min_num = new_array[index - 1]                          # и определяем, какое из них ближе
            max_num = new_array[index + 1]
            if X - min_num > max_num - X:
                print(f"Ближайшее число -> {max_num}")
            elif X - min_num == max_num - X:
                print(f"Ближайшие числа -> {min_num}, {max_num}")
            else:
                print(f"Ближайшее число -> {min_num}")
        elif index == 0:                                            # Если число стоит на первом или последнем месте,
            nearest = new_array[index + 1]                          # то просто берем соседнее
            print(f"Ближайшее число -> {nearest}")
        elif index == len(new_array) - 1:
            nearest = new_array[index - 1]
            print(f"Ближайшее число -> {nearest}")
        break
    index += 1






