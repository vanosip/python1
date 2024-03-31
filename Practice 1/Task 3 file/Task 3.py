# На вход программе подаётся путь к файлу с расширением txt, где на каждой новой строке содержатся информация с
# именами участников конкурса и их баллами. Значения в строке
# могут быть разделены любым количеством пробелов.
# Пример файла:
# Василий 70
# Светлана 90
# Алиса 60
# Считайте информацию из файла, а затем выполните следующие задачи:
# • Отсортируйте участников конкурса по имени, результат
# выведите на консоль.
# • Отсортируйте участников конкурса по количеству
# набранных баллов, результат выведите на консоль.
# • Выведите в файл res.txt имена только тех участников, чей
# результат превышает значение N, введённое пользователем.
# Для решения задач необходимо использовать функции высшего порядка.


print('Enter name file ___.txt')
name_file = input()
try:
    with open(name_file, 'r', encoding='utf-8') as file:
        data = [line.rstrip(' ').split() for line in file]
except FileNotFoundError:
    print("A file with that name was not found")
for i in range(len(data)):
    try:
        data[i][1] = int(data[i][1])
    except ValueError:
        print('data error')
        exit(0)
print('Mode selection\n'
      '1 - Sorting by name\n'
      '2 - Sorting by points\n'
      '3 - Sorting by the entered score')
try:
    select_mode = int(input())
    if select_mode != 1 and select_mode != 2 and select_mode != 3:
        print("There is no such mode")
        exit(0)
    if select_mode == 3:
        print("Enter a natural number N relative to sort ")
        try:
            N = int(input())
        except ValueError:
            print("The entered character is not a number")
            exit(0)
except ValueError:
    print("The entered character is not a number")
    exit(0)

data = dict(data)
if select_mode == 1:
    sorted_data = sorted(data.items(), key=lambda x: x[0])
    for i in range(len(sorted_data)):
        print(*list(sorted_data[i]), sep=' ')
elif select_mode == 2:
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(sorted_data)):
        print(*list(sorted_data[i]), sep=' ')
else:
    sorted_data = dict(filter(lambda item: int(item[1]) >= N, data.items()))
    data1 = list(sorted_data)
    with open('res.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data1)):
            file.write(data1[i] + '\n')
    print("The result has been successfully written to a file res.txt")
