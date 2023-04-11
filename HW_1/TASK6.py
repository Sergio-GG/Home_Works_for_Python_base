# Написать программу, которая определяет, является ли билет счастливым
sum = 0
sum_2 = 0
index = 0
ticket = input("Введите шестизначный номер билета: ")
if len(ticket) == 6:
    for i in ticket:
        if index < 3:
            sum += int(i)
        else:
            sum_2 += int(i)
        index += 1

    if sum == sum_2:
        print("Билет счастливый")
    else:
        print("Билет обычный")
else:
    print("Введите корректный номер билета")
