# Найдите сумму цифр трехзначного числа

sum = 0
number = input("Введите трехначное число: ")
for i in number:
    sum += int(i)
print(f"Сумма цифр числа {number} равна {sum}")
