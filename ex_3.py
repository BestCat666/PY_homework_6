# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#list comprehension
import math

lst = list(map(float, input('Введите элементы массива через пробел: ').split()))
print(lst)
lst_res = [round((lst[i] - int(lst[i])), 3) for i in range(len(lst))]
print(lst_res)
print('разницa между максимальным и минимальным значением дробной части элементов =', max(lst_res) - min(lst_res))
