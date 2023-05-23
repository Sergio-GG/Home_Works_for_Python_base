# Задача 34. Определить ритмичность стихов Винни-Пуха

word = input("Введите считалку Винни-Пуха: ")
a = word.split()
print(a)


def vowels(wrd):
    count = 0
    b = ["а", "о", "у", "е", "и", "э", "ы", "ё", "ю", "я"]
    for letter in wrd:
        if letter in b:
            count += 1
    return count


def same_number(func, obj: list):
    lst = []
    for i in obj:
        lst.append(func(i))
    return all(item == lst[0] for item in lst)


if same_number(vowels, a):
    print("Парам пам-пам")
else:
    print("Пам парам")
