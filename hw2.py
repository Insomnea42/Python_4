# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def getresult(n):
    i = 2
    list = []
    while i * i <= n:
        while n % i == 0:
            list.append(i)
            n = round(n / i)
        i += 1
    if n > 1:
        list.append(n)
    return list

n = int(input('Введите число: '))
list = []
list = getresult(n)
print(list)
