"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k."""

coef = [2,4,7,8]
n = len(coef)
for i in range(n):
    print(coef[i], end='')
    if i != 0:
        print("x^", i, end='', sep='')
    if i != n-1:
        print(" + ", end='')