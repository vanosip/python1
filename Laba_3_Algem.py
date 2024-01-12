import re
"""""""""
def degree_nep(degree, pol):
    degree_1 = degree
    for i in range(degree):
        if pol[0] == 0:
            pol.pop(0)
            degree = degree - 1
    return degree
"""""


def nod(a, b):#НОД двух чисел

    while b:
        a, b = b, a % b
    return a

def sturm_create(pol):
    sequence = [pol, proizvodnai(pol)]

    while sequence[-1]:
        quotient, remainder = delenie_1(sequence[-2], sequence[-1])
        sequence.append([-x for x in remainder])

    return sequence

def delenie_1(delimoe, delitel):
    quotient = [0] * (len(delimoe) - len(delitel) + 1)
    temp_dividend = list(delimoe)

    for i in range(len(delimoe) - len(delitel), -1, -1):
        ratio = temp_dividend[i + len(delitel) - 1] / delitel[-1]
        quotient[i] = ratio

        for j in range(len(delitel)):
            temp_dividend[i + j] -= ratio * delitel[j]

    remainder = temp_dividend[:len(delitel) - 1]
    return quotient, remainder



def vvod(input_str):
    # проверка на наличие посторонних символов
    if not re.match(r'^[0-9xX^+\-\s]+$', input_str):
        raise ValueError("Введены недопустимые символы в многочлене.")

    # Извлекаем слагаемые многочлена с использованием регулярных выражений
    terms = re.split(r'(?=[+-])', input_str)

    # словарь для хранения коэффициентов
    coefficients = {}

    max_degree = 0  # Переменная для степени

    for term in terms:
        # разделяем слагаемое на коэффициент и степень
        match = re.match(r'([-+]?\d*)x(?:\^(\d+))?', term)
        if match:
            coefficient = match.group(1)
            if coefficient == '' or coefficient == '+':
                coefficient = 1
            elif coefficient == '-':
                coefficient = -1
            else:
                coefficient = int(coefficient)

            exponent = match.group(2)
            if exponent is None:
                exponent = 1
            else:
                exponent = int(exponent)

            # обновим переменную для проверки наибольшей степени
            max_degree = max(max_degree, exponent)

            # Добавляем коэффициент в словарь
            if exponent in coefficients:
                coefficients[exponent] += coefficient
            else:
                coefficients[exponent] = coefficient
        else:
            # если  не соответствует  x^k, то это свободный член
            coefficients[0] = int(term)



        #словарь в список коэффициентов (в убывающем порядке степеней)
    degree = max(coefficients.keys())
    result_coefficients = [coefficients.get(exp, 0) for exp in range(degree, -1, -1)]

    return result_coefficients ,max_degree


def interval(pol):
    l = len(pol)
    #print('len pol = ',l)
    sp=[]
    for i in range(l):
        #print('i = ',i)
        if i == 0 :
            continue
        s = abs( pol[i] / pol[0])
        sp.append(s)
    c = max(sp)+1
    inter = [-c,c]
    return inter
    #print(c)
   # print(sp)

def count_sign(sequence, x):

    #считает  изменения знака в ряду штурма для заданной точки x
    signs = [sum(c * x**i for i, c in enumerate(poly)) for poly in sequence if poly]
    sign_changes = sum(1 for a, b in zip(signs, signs[1:]) if a * b < 0)
    return sign_changes

def sturm_roots(sequence, interval):#Считает количество корней в заданном интервале


     a, b = interval
     sign_changes_a = count_sign(sequence, a)
     sign_changes_b = count_sign(sequence, b)

     return abs(sign_changes_a - sign_changes_b)


"""
def NOD_Pol(delimoe,delitel):
    x = delitel.copy()
    dst=delenie(delimoe.copy(),x.copy())
    while True:
       # print(dst)
        ostat = dst[1]
        #print('ostat = ',ostat)
        if ostat == []:
            return x
        else:
            ostat.reverse()
            #print('reverse ostat = ',ostat)
           # print('x = ',x)
            dst = delenie(x.copy(),ostat.copy())
            x=ostat
"""

"""
def delenie(a,b):
    a.reverse()
    b.reverse()
    result, l1 = [], len(b)  ## список под результат, длина делителя
    while True:
        l, k = len(a), l1 - 1  ## длина делимого; переменная, нужная позже
        multiplier = a[-1] / b[-1]  ## вычисляем множитель, который убьёт старший многочлен
        for i in range(l - 1, l - (l1 + 1), -1):
            a[i] = a[i] - multiplier * b[k]
            k -= 1  ## с помощью переменной k двигаемся по списку коэф. делителя
        q = -1  ## один всегда насчитает
        for i in range(l - 1, -1, -1):  ## убираем все нули с начала списка коэф.
            if a[i] == 0:
                a = a[:-1]
                q += 1  ## каждый раз добавляем, как только нуль
            else:
                break
        result.append(multiplier)  ## добавили множитель
        for _ in range(q):  ## если что-то насокращалось, то добить нулями
            result.append(0)
        if len(a) < len(b):  # если старшая степень делимого меньше старшней степени делителя
            break
    while result[-1] == 0:  ## если поделился нацело в конце, то нулей вкинут, а нам не надо
        result = result[:-1]
    return result[::-1], a

"""



def proizvodnai (x):
    l = len(x)-1
    poll = x.copy()
    for i in range(len(poll)):
        poll[i] = poll[i] * l
        l = l-1
    poll.pop(len(poll)-1)
    return poll
# def vivod_pol(pol):
#     print('Вы ввели многочлен ')
#     degree_1 = len(pol)-1
#     for x in pol:
#         if x == 0:
#             degree_1=degree_1-1
#             continue
#         if len(pol)-1 == 1 and degree_1==len(pol)-1:
#             print('{}x'.format(x),end='')
#             degree_1=degree_1-1
#             continue
#         if degree_1 == 0:
#             if x > 0:
#                 print('+{}'.format(x),end='')
#             elif x == 1:
#                 print('+{}'.format(x), end='')
#             else:
#                 print('{}'.format(x))
#             continue
#         if degree_1 == len(pol)-1 and degree_1 != 1:
#             print('{}x^{}'.format(x, degree_1), end='')
#             degree_1 = degree_1 - 1
#             continue
#         else:
#             if x > 0:
#                 if degree_1 == 1:
#                     print('+{}x'.format(x, degree_1), end='')
#                 else:
#                     print('+{}x^{}'.format(x, degree_1),end='')
#             elif(x<0):
#                 if(degree_1 == 1):
#                     print('{}x'.format(x, degree_1), end='')
#                 else:
#                     print('{}x^{}'.format(x, degree_1), end='')
#         degree_1 = degree_1 - 1
#     print('\n')










############ main #############################################################








polin = input('Enter polinom x^2-1 ')
pol, degree = vvod(polin)
print('Степень многочлена = ',degree)

#while 1:
#    try:
#        degree = int(input('Введите степень многочлена '))
#        break
#    except ValueError:
#        print('Try again')
#if degree == 0:
#   print("Don't polinom")
#    exit()
#print('Степень многочлена = ', degree)
#print('Введите коэффициэнты многочлена')
#pol = list(int(x) for x in input().split())
#print(pol)
#if len(pol) > degree+1:
#    print('Error count')
#    exit()
#elif len(pol) < degree+1:
#    print('Error count')
#   exit()
#if pol[0] == 0:
#    print('Внимание! Изменилась степень многочлена')
#    degree = degree_nep(degree, pol)
#    print(degree)
#    if degree == 0:
#        print("Don't polinom")
#vivod_pol(pol)

while 1:
    try:
        apro = int(input('Введите коэфициэнт апроксимации '))
        break
    except ValueError:
        print('Try again')

#################### math ###############################################################
intA_B=interval(pol.copy())
print('Интервал на котором существуют корни ',intA_B)
sequence=sturm_create(pol)
l_1=len(sequence)
for i in range(l_1-1):
    print('f_{}(x) = '.format(i), sequence[i])
print('На интервале',intA_B,'существует ',sturm_roots(sequence,intA_B),' корней')









