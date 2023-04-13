# Перевернуть минимальное количество монет

import random
counter = 0
N = int(input("Введите количество монеток"))
for i in range(N):
    temp = random.randint(0, 1)
    print(temp)
    if temp == 0:
        counter += 1
if counter <= N // 2:
    print(f"Нужно перевернуть {counter} монет")
else:
    print(f"Нужно перевернуть {N - counter} монет")
