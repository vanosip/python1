# 2. Существует математическая гипотеза, которая строится на предположении, что любое натуральное
# число N может быть превращено в 1 в результате последовательного выполнения следующих действий:
# • если оно чётное, то делим его на 2
# • если нечётное, то умножаем на 3 и прибавляем 1
# Над полученным числом вышеописанные действия выполняются вновь до тех пор, пока не получится 1.
# Пример: 16 -> 8 -> 4 -> 2 -> 1
#  13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Пиком последовательности называют наибольшее из чисел,
# полученных в процессе преобразования числа N в 1. В примере
# пик последовательности отмечен красным.
# Напишите программу, которая принимала бы на вход число N,
# а затем выводила бы на консоль саму последовательность,
# количество элементов в последовательности и её пик


# ///////////////////////////////////////////////////////////////////
way = []


def transformation(numberr):
    if numberr == 1:
        way.append(numberr)
        return 0
    way.append(numberr)
    if numberr % 2 == 0:
        transformation(numberr // 2)
    else:
        transformation(numberr * 3 + 1)


# def beautiful_out(wayy, max_wayy):
#     if wayy[0] == max_wayy:
#         print("\033[1;31m{}\033[0m".format(wayy[0]), end='->')
#     else:
#         print(wayy[0], end='->')
#     wayy.pop(0)
#     for i in wayy:
#         if i == max_wayy:
#             print("\033[1;31m{}\033[0m".format(i), end='->')
#             continue
#         else:
#             print(str(i),end='')


while True:
    try:
        number = int(input("Введите  натуральное число "))
        break
    except ValueError:
        print("The number is not natural")
        print("Try again")
# print("\033[1;31mТекст красного цвета\033[0m")
transformation(number)

max_way = max(way)
print("Here is the complete chain of transformation")
print('Number of elements - ', len(way))
print("The peak of the sequence - ", max_way)
str_out = "->".join(map(lambda x: str(x), way))
print(str_out)
