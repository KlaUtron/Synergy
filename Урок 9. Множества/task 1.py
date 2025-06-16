try:
    N =  int(input('Ведите число (1<=N<=100000) '))
    if N < 1 or 1 > 100000:
        raise ValueError('N должно быть не меньше 1 и не больше 10000')
except ValueError as e:
    print(f'Ошибка; {e}')
    exit()

num_str = input('Введите число через пробел ').split()
if len(num_str) != N:
    print(f'Ошибка: Введено {len(num_str)} чисел между {N}')
    exit()
    
try:
    numbers = list(map(int, num_str))
except ValueError:
    print("Ошибка: Введены некорректные данные (не целые числа).")
    exit()

for num in numbers:
    if abs(num) > 2 * 10**9:
        print(f"Ошибка: Число {num} превышает 2*10^9 по модулю.")
        exit()

unique_numbers = set(numbers)
print("Количество уникальных чисел:", len(unique_numbers))