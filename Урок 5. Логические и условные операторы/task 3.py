num = int(input("Cтартап - "))
Mike = int(input("Майл вложил - "))
Ivan = int(input("Иван вложил - "))

if Mike >= num and Ivan >= num:
    print(2)
elif Mike + Ivan < num:
    print(0)
elif Mike + Ivan >= num:
    print(1)