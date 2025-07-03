def factorial(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def get_factorial_sequence(n):
    initial_factorial = factorial(n)
    factorial_list = []
    for num in range(initial_factorial, 0, -1):
        factorial_list.append(factorial(num))

    return factorial_list

number = int(input('Введите натуральное число '))
res = get_factorial_sequence(number)
print(f'Список факториалов: {res}')