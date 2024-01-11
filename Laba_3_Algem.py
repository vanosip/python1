def degree_nep(degree, pol):
    degree_1 = degree
    for i in range(degree):
        if pol[0] == 0:
            pol.pop(0)
            degree = degree - 1
    return degree

def vivod_pol(pol):
    print('Вы ввели многочлен ')
    degree_1 = len(pol)-1
    for x in pol:
        if x ==0:
            degree_1=degree_1-1
            continue
        if degree_1 == 0:
            print('{}'.format(x),end='')
        if degree_1 == len(pol)-1:
            print('{}x^{}'.format(x, degree_1), end='')
            degree_1 = degree_1 - 1
            continue
        else:
            if(x>0):
                if(degree_1==1):
                    print('+{}x'.format(x, degree_1), end='')
                else:
                    print('+{}x^{}'.format(x, degree_1),end='')
            elif(x<0):
                if(degree_1==1):
                    print('{}x'.format(x, degree_1), end='')
                else:
                    print('{}x^{}'.format(x, degree_1), end='')
        degree_1 = degree_1 - 1

##### main #########################################
while 1:
    try:
        degree = int(input('Введите степень многочлена '))
        break
    except ValueError:
        print('Try again')
#print('Степень многочлена = ', degree)
print('Введите коэффициэнты многочлена')
pol = list(int(x) for x in input().split())
print(pol)
if pol[0] == 0:
    print('Внимание! Изменилась степень многочлена')
    degree = degree_nep(degree, pol)
    print(degree)
vivod_pol(pol)
