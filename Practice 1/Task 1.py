# 1. Пользователь вводит 10 слов, разделённых точкой с запятой, а
# затем контрольную строку на отдельной строке. Выведите
# только те слова, которые начинаются с контрольной строки.

# ///////////////////////////////////////////////////////////////
# Hello;Gena;Dog;god;Hell;bed;bathroom;seven;eight;thousend
input_str = input().split(';')
if len(input_str) == 0:
    print("The entered line is empty")
    exit(0)
if len(input_str) != 10:
    exit(0)
cont_str = input()
if len(cont_str) == 0:
    print("The entered control line is empty")
    exit(0)
result = []
for i in input_str:
    # if input_str[i][:len(cont_str)] == cont_str:
    if i.startswith(cont_str):
        result.append(i)
if len(result) == 0:
    print("None")
print(*result)
