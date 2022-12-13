# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#filter, lambda
lst = list(map(int, input('Введите элементы массива через пробел: ').split()))
print(lst)
lst2 = list(filter(lambda x: lst.count(x) == 1, lst))
print('Неповторяющиеся элементы', lst2)



# было:
# lst = list(map(int, input('Введите элементы списка через пробел: ').split()))
# print(lst)
# unique_num = []
# #lst = set(lst)
# #print(set(lst))
# #print(lst)
# for i in range(len(lst)):
#     if lst.count(lst[i]) == 1:
#         unique_num.append(lst[i])
# print(unique_num)