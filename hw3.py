# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

posl = [12, 34, 65, 6, 44, 44, 44, 45, 6]
list = []
for i in posl:
    if i not in list:
        list.append(i)

print(f'Исходная последовательность: {posl}')
print(f'Список неповторяющихся элементов: {list}')