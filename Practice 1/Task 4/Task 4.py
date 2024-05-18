# #На вход подаётся путь к файлу с расширением .txt, в котором содержится
# текст.Напишите программу, которая подсчитывала бы частоту встречаемости символов в
# тексте без учёта регистра, а затем выводила бы результат в файл res.txt в формате
# символ: частота встречаемости
# Пример:
# Входной файл:              res.txt
# Мама                       м: 2
#                            а: 2


print("Specify the name (path) of the file")
name_file = input()
symbol_dict = {}
try:
    with open(name_file, 'r', encoding='utf-8') as file:
        text = file.readlines()
except FileNotFoundError:
    print("The specified file was not found or an error occurred when opening it")
if len(text) == 0:
    print('The file is empty')
    exit(0)
text = [x.lower() for x in text]
for i in range(len(text)):
    for symbol in text[i]:
        if symbol == '\n' or symbol == '':
            continue
        if symbol in symbol_dict:
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
if len(symbol_dict) == 0:
    print('The file is empty')
    exit(0)

# basis = set()
# for x in text:
#     basis = basis.union(set(x))
#
# basis.remove(' ')
# basis.remove('\n')
# dict_symbols = []
# for i in basis:
#     t = 0
#     for g in text:
#         t += g.count(i)
#     dict_symbols.append([i, t])
with open('res.txt', 'w', encoding='utf-8') as file:
    for symbol, count_symbol in symbol_dict.items():
        file.write(f'{symbol}:{count_symbol}\n')
print("The result has been successfully written to a file res.txt")
