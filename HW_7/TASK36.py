# Задача 36. Вывести таблицу с помощью функции высшего порядка.
# Написать функцию print_operation_table()


def print_operation_table(operator, num_rows, num_columns):
    for i in range(1, num_columns + 1):
        print(i, end="\t")
        for j in range(2, num_rows + 1):
            print(operator(i, j), end="\t")
        print(end="\n")


print_operation_table(lambda x, y: x * y, num_rows=6, num_columns=6)
