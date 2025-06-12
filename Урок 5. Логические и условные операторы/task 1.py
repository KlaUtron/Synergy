num = int(input("Введите число: "))

if num == 0:
    print("Ваше число равно нулю")
elif num < 0 and num % 2 == 0:
    print("Ваше число отрицательное и четное")
elif num > 0 and num % 2 == 0:
    print("Ваше число положительное и четное")
elif num < 0 and num % 2:
    print("Ваше число отрицательное и нечетное")
elif num > 0 and num % 2:
    print("Ваше число положительное и нечетное")