# 2. Существует математическая гипотеза, которая строится на предположении, что любое натуральное число N может быть
# превращено в 1 в результате последовательного выполнения следующих действий:
# • если оно чётное, то делим его на 2
# • если нечётное, то умножаем на 3 и прибавляем 1
# Над полученным числом вышеописанные действия
# выполняются вновь до тех пор, пока не получится 1.
# Пример: 16 -> 8 -> 4 -> 2 -> 1
#  13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Пиком последовательности называют наибольшее из чисел,
# полученных в процессе преобразования числа N в 1. В примере
# пик последовательности отмечен красным.
# Напишите программу, которая принимала бы на вход число N,
# а затем выводила бы на консоль саму последовательность,
# количество элементов в последовательности и её пик


#///////////////////////////////////////////////////////////////////
way = []
def transformation(number):
    if (number == 1):
        way.append(number)
        return 0
    way.append(number)
    if (number % 2 == 0):
        transformation(number//2)
    else:
        transformation(number*3+1)


def beautiful_out(way, max_way):
    if (way[0] == max_way):
        print("\033[1;31m{}\033[0m".format(way[0]),end='->')
    else:
        print(way[0],end='->')
    way.pop(0)
    for i in range(len(way)):
        if(way[i] == max_way):
            print("\033[1;31m{}\033[0m".format(way[i]),end='->')
            continue
        if(i != len(way)-1):
            print(way[i], end='->')
        else:
            print(way[i])


while True:
    try:
        number = int(input("Введите  натуральное число "))
        break
    except ValueError:
        print("The number is not natural")
        print("Try again")
#print("\033[1;31mТекст красного цвета\033[0m")
transformation(number)
max_way = max(way)
print("Here is the complete chain of transformation")
beautiful_out(way,max_way)
