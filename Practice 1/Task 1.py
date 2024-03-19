#1. Пользователь вводит 10 слов, разделённых точкой с запятой, а
#затем контрольную строку на отдельной строке. Выведите
#только те слова, которые начинаются с контрольной строки.

#///////////////////////////////////////////////////////////////
#Hello;Gena;Dog;god;Hell;bed;bathroom;seven;eight;thousend
input_str = input().split(';')
cont_str = input()
result = []
for i in range(10):
    if(input_str[i][:len(cont_str)] == cont_str):
        result.append(input_str[i])
print(result)