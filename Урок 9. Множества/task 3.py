num_str = input().split()
tmp = set()
res = []

for i in num_str:
    try:
        num = int(i)
    except ValueError:
        
        try:
            num = float(i)
        except ValueError:
            print(f"Ошибка: '{num_str}' не является числом.")
            exit()
    if num in tmp:
        res.append("Yes")
    else:
        res.append("No")
        tmp.add(num)

print("\n".join(res))