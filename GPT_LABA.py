# def gcd(a, b):
#     """
#     Находит наибольший общий делитель двух чисел.
#
#     :param a: Первое число.
#     :param b: Второе число.
#     :return: Наибольший общий делитель a и b.
#     """
#     while b:
#         a, b = b, a % b
#     return a
#
# def evaluate_derivative(coefficients):
#     """
#     Вычисляет коэффициенты производной полинома.
#
#     :param coefficients: Список коэффициентов полинома (в убывающем порядке степеней).
#     :return: Список коэффициентов производной полинома.
#     """
#     derivative_coefficients = [i * c for i, c in enumerate(coefficients)][1:]
#     return derivative_coefficients
#
# def synthetic_division(dividend, divisor):
#     """
#     Синтетическое деление полиномов.
#
#     :param dividend: Делимое (список коэффициентов полинома).
#     :param divisor: Делитель (список коэффициентов многочлена).
#     :return: Частное и остаток от деления.
#     """
#     quotient = [0] * (len(dividend) - len(divisor) + 1)
#     temp_dividend = list(dividend)
#
#     for i in range(len(dividend) - len(divisor), -1, -1):
#         ratio = temp_dividend[i + len(divisor) - 1] / divisor[-1]
#         quotient[i] = ratio
#
#         for j in range(len(divisor)):
#             temp_dividend[i + j] -= ratio * divisor[j]
#
#     remainder = temp_dividend[:len(divisor) - 1]
#     return quotient, remainder
#
# def generate_sturm_sequence(coefficients):
#     """
#     Генерирует последовательность Ряда Штурма для полинома.
#
#     :param coefficients: Список коэффициентов полинома (в убывающем порядке степеней).
#     :return: Список полиномов, образующих Ряд Штурма.
#     """
#     sequence = [coefficients, evaluate_derivative(coefficients)]
#
#     while sequence[-1]:
#         quotient, remainder = synthetic_division(sequence[-2], sequence[-1])
#         sequence.append([-x for x in remainder])
#
#     return sequence
#
# def find_roots_using_bisection(sequence, interval, tolerance=1e-6, max_iterations=100):
#     """
#     Находит корни полинома в заданном интервале с использованием метода бисекции.
#
#     :param sequence: Ряд Штурма (список полиномов).
#     :param interval: Интервал [a, b], где ищутся корни.
#     :param tolerance: Точность (по умолчанию 1e-6).
#     :param max_iterations: Максимальное количество итераций (по умолчанию 100).
#     :return: Список приближенных корней полинома в заданном интервале.
#     """
#     roots = []
#
#     for i in range(len(sequence) - 1):
#         a, b = interval
#         sign_changes_at_a = count_sign_changes(sequence[:i+1], a)
#         sign_changes_at_b = count_sign_changes(sequence[:i+1], b)
#
#         if sign_changes_at_a != sign_changes_at_b:
#             root = bisection_method(sequence[i], interval, tolerance, max_iterations)
#             roots.append(root)
#
#     return roots
# def count_sign_changes(sequence, x):
#     """
#     Подсчитывает количество изменений знака в Ряде Штурма для заданной точки x.
#
#     :param sequence: Ряд Штурма (список полиномов).
#     :param x: Значение, для которого подсчитываются изменения знака.
#     :return: Количество изменений знака.
#     """
#     signs = [sum(c * x**i for i, c in enumerate(poly)) for poly in sequence if poly]
#     sign_changes = sum(1 for a, b in zip(signs, signs[1:]) if a * b < 0)
#     return sign_changes
#
# def sturm_theorem_roots(sequence, interval):
#     """
#     Находит количество корней полинома в заданном интервале с использованием Теоремы Штурма.
#
#     :param sequence: Ряд Штурма (список полиномов).
#     :param interval: Интервал [a, b], где ищутся корни.
#     :return: Количество корней в заданном интервале.
#     """
#     a, b = interval
#     sign_changes_at_a = count_sign_changes(sequence, a)
#     sign_changes_at_b = count_sign_changes(sequence, b)
#
#     return sign_changes_at_a - sign_changes_at_b
#
# # Пример использования
# polynomial_coefficients = [1,-6,3]  # Пример: x^3 - 3x^2 + 1
# sturm_sequence = generate_sturm_sequence(polynomial_coefficients)
# print(generate_sturm_sequence(polynomial_coefficients))
# interval = [-5, 0]
# roots_count = sturm_theorem_roots(sturm_sequence, interval)
#
# print(f"Количество корней в заданном интервале: {roots_count}")
import  re
def evaluate_polynomial(coefficients, x):
    return sum(c * x**i for i, c in enumerate(coefficients))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def evaluate_derivative(coefficients):
    derivative_coefficients = [i * c for i, c in enumerate(coefficients)][1:]
    return derivative_coefficients

def synthetic_division(dividend, divisor):
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    temp_dividend = list(dividend)

    for i in range(len(dividend) - len(divisor), -1, -1):
        ratio = temp_dividend[i + len(divisor) - 1] / divisor[-1]
        quotient[i] = ratio

        for j in range(len(divisor)):
            temp_dividend[i + j] -= ratio * divisor[j]

    remainder = temp_dividend[:len(divisor) - 1]
    return quotient, remainder

def generate_sturm_sequence(coefficients):
    sequence = [coefficients, evaluate_derivative(coefficients)]

    while sequence[-1]:
        quotient, remainder = synthetic_division(sequence[-2], sequence[-1])
        sequence.append([-x for x in remainder])

    return sequence

def count_sign_changes(sequence, x):
    signs = [evaluate_polynomial(poly, x) for poly in sequence if poly]
    sign_changes = sum(1 for a, b in zip(signs, signs[1:]) if a * b < 0)
    return sign_changes

def sturm_theorem_roots(sequence, interval, tolerance=1e-6, max_iterations=100):
    a, b = interval
    sign_changes_at_a = count_sign_changes(sequence, a)
    sign_changes_at_b = count_sign_changes(sequence, b)

    return sign_changes_at_a - sign_changes_at_b

def bisection_method(coefficients, interval, tolerance=1e-6, max_iterations=100):
    a, b = interval

    if evaluate_polynomial(coefficients, a) * evaluate_polynomial(coefficients, b) > 0:
        raise ValueError("Метод бисекции требует, чтобы функция меняла знак на концах интервала.")

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        if evaluate_polynomial(coefficients, c) == 0:
            return c
        elif evaluate_polynomial(coefficients, c) * evaluate_polynomial(coefficients, a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2

def find_roots_using_bisection(sequence, interval, tolerance=1e-6, max_iterations=100):
    roots = []

    for i in range(len(sequence) - 1):
        a, b = interval
        sign_changes_at_a = count_sign_changes(sequence[:i+1], a)
        sign_changes_at_b = count_sign_changes(sequence[:i+1], b)

        if sign_changes_at_a != sign_changes_at_b:
            root = bisection_method(sequence[i], interval, tolerance, max_iterations)
            roots.append(root)

    return roots

def vvod(input_str):
    # Проверка на наличие посторонних символов
    if not re.match(r'^[0-9xX^+\-\s]+$', input_str):
        raise ValueError("Введены недопустимые символы в многочлене.")

    # Извлекаем слагаемые многочлена с использованием регулярных выражений
    terms = re.split(r'(?=[+-])', input_str)

    # Инициализируем словарь для хранения коэффициентов
    coefficients = {}

    max_degree = 0  # Переменная для отслеживания наибольшей степени

    for term in terms:
        # Разделяем слагаемое на коэффициент и степень
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

            # Обновляем переменную для отслеживания наибольшей степени
            max_degree = max(max_degree, exponent)

            # Добавляем коэффициент в словарь
            if exponent in coefficients:
                coefficients[exponent] += coefficient
            else:
                coefficients[exponent] = coefficient
        else:
            # Если слагаемое не соответствует формату x^k, то это свободный член
            coefficients[0] = int(term)

    #print(f"Cтепень многочлена: {max_degree}")

    # Преобразуем словарь в список коэффициентов (в убывающем порядке степеней)
    degree = max(coefficients.keys())
    result_coefficients = [coefficients.get(exp, 0) for exp in range(degree, -1, -1)]

    return result_coefficients ,max_degree




# Ввод пользователем коэффициентов полинома
degree = int(input("Введите степень полинома: "))

coefficients = vvod(input())

# Ввод пользователем интервала и точности
interval_start = float(input("Введите начало интервала: "))
interval_end = float(input("Введите конец интервала: "))
tolerance = float(input("Введите желаемую точность для аппроксимации корней: "))

interval = [interval_start, interval_end]

    # Генерация Ряда Штурма
sturm_sequence = generate_sturm_sequence(coefficients)

    # Вывод Ряда Штурма
print("\nРяд Штурма:")
for poly in sturm_sequence:
    print(poly)

    # Поиск корней с использованием метода бисекции
roots = find_roots_using_bisection(sturm_sequence, interval, tolerance)

    # Вывод найденных корней
print("\nНайденные корни:")
for root in roots:
    print(f"{root:.6f}")

