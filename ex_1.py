#1.Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#enumerate, map
lst = list(map(int, input('Введите элементы массива через пробел: ').split()))
print(lst)
res = 0
for index, value in enumerate(lst):
    if index != 0 and index % 2 != 0:
        res = res + value
print(res)

# было:
#  lst = list(map(int, input('Введите элементы массива через пробел: ').split()))
# print(lst)
# res = 0
# for i in range(len(lst)):
#     if i != 0 and i % 2 != 0:
#         res = res + lst[i]
#         print('на нечётной позиции элемент ', lst[i])
# print('сумма элементов на нечётных позициях = ', res)



